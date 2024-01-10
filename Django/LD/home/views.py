import cv2
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

import os, io
import csv
import random
import numpy as np
import pandas as pd
from skimage import measure
from skimage.transform import resize
from PIL import Image

import tensorflow as tf
from tensorflow import keras

import matplotlib
matplotlib.use('Agg')  # Add this line before importing pyplot

from matplotlib import pyplot as plt

import matplotlib.patches as patches

model_path=os.path.join(settings.BASE_DIR,'model.h5')

class generator(keras.utils.Sequence):

    def __init__(self, folder, filenames, pneumonia_locations=[], batch_size=32, image_size=256, shuffle=True, augment=False, predict=False):
        self.folder = folder
        self.filenames = filenames
        self.pneumonia_locations = pneumonia_locations
        self.batch_size = batch_size
        self.image_size = image_size
        self.shuffle = shuffle
        self.augment = augment
        self.predict = predict
        self.on_epoch_end()

    def __load__(self, filename):
        # load image file as numpy array
        img = np.asarray(Image.open(os.path.join(self.folder, filename)))
        # create empty mask
        msk = np.zeros(img.shape)
        # get filename without extension
        filename = filename.split('.')[0]
        # if image contains pneumonia
        if filename in self.pneumonia_locations:
            # loop through pneumonia
            for location in self.pneumonia_locations[filename]:
                # add 1's at the location of the pneumonia
                x, y, w, h = location
                msk[y:y+h, x:x+w] = 1.0
        # resize both image and mask
        img = resize(img, (self.image_size, self.image_size), mode='reflect')
        msk = resize(msk, (self.image_size, self.image_size), mode='reflect') > 0.5
        # if augment then horizontal flip half the time
        if self.augment and random.random() > 0.5:
            img = np.fliplr(img)
            msk = np.fliplr(msk)
            # add trailing channel dimension
        img = np.expand_dims(img, -1)
        msk = np.expand_dims(msk, -1)
        return np.array(img), np.array(msk)

    def __loadpredict__(self, filename):
        # load jpg file as numpy array
        img = np.asarray(Image.open(os.path.join(self.folder, filename)))
        # resize image
        img = resize(img, (self.image_size, self.image_size), mode='reflect')
        # add trailing channel dimension
        img = np.expand_dims(img, -1)
        return img

    def __getitem__(self, index):
        # select batch
        filenames = self.filenames[index*self.batch_size:(index+1)*self.batch_size]
        # predict mode: return images and filenames
        if self.predict:
            # load files
            imgs = [self.__loadpredict__(filename) for filename in filenames]
            # create numpy batch
            imgs = np.array(imgs)
            return imgs, filenames
        # train mode: return images and masks
        else:
            # load files
            items = [self.__load__(filename) for filename in filenames]
            # unzip images and masks
            imgs, msks = zip(*items)
             # create numpy batch
            imgs = np.array(imgs)
            msks = np.array(msks)
            return imgs, msks

    def on_epoch_end(self):
        if self.shuffle:
            random.shuffle(self.filenames)

    def __len__(self):
        if self.predict:
            # return everything
            return int(np.ceil(len(self.filenames) / self.batch_size))
        else:
            # return full batches only
            return int(len(self.filenames) / self.batch_size)
        
# define iou or jaccard loss function
def iou_loss(y_true, y_pred):
    y_true = tf.reshape(y_true, [-1])
    y_pred = tf.reshape(y_pred, [-1])
    y_true = tf.cast(y_true, tf.float32)
    y_pred = tf.cast(y_pred, tf.float32)
    intersection = tf.reduce_sum(y_true * y_pred)
    score = (intersection + 1.) / (tf.reduce_sum(y_true) + tf.reduce_sum(y_pred) - intersection + 1.)
    return 1 - score

# combine bce loss and iou loss
def iou_bce_loss(y_true, y_pred):
    return 0.5 * keras.losses.binary_crossentropy(y_true, y_pred) + 0.5 * iou_loss(y_true, y_pred)

# mean iou as a metric
def mean_iou(y_true, y_pred):
    y_pred = tf.round(y_pred)
    intersect = tf.reduce_sum(y_true * y_pred, axis=[1, 2, 3])
    union = tf.reduce_sum(y_true, axis=[1, 2, 3]) + tf.reduce_sum(y_pred, axis=[1, 2, 3])
    smooth = tf.ones(tf.shape(intersect))
    return tf.reduce_mean((intersect + smooth) / (union - intersect + smooth))

def cosine_annealing(x):
    lr = 0.001
    epochs = 25
    return lr*(np.cos(np.pi*x/epochs)+1.)/2
learning_rate = tf.keras.callbacks.LearningRateScheduler(cosine_annealing)

def recieve_preds(image_name):
    with tf.keras.utils.custom_object_scope({'iou_bce_loss':iou_bce_loss,'mean_iou':mean_iou}):
        loaded_model = tf.keras.models.load_model(model_path)
    
    valid_filenamess=[image_name]
    
    folders = os.path.join(settings.MEDIA_ROOT,'downloads')
    test_gen = generator(folders, valid_filenamess, batch_size=1, image_size=256, shuffle=False, predict=False)
    
    for imgs, msks in test_gen:
        # predict batch of images
        preds = loaded_model.predict(imgs)
        # create figure
        f, axarr = plt.subplots(1, 1, figsize=(20,15))
        # axarr = axarr.ravel()
        # axidx = 0
        # loop through batch
        for img, msk, pred in zip(imgs, msks, preds):
            # plot image
            # axarr[axidx].imshow(img[:, :, 0])
            axarr.imshow(img[:, :, 0])
            # threshold predicted mask
            comp = pred[:, :, 0] > 0.5
            # apply connected components
            comp = measure.label(comp)
            confidence_scores = (pred[:, :, 0] > 0.5).astype(np.uint8)
            
            confidence_scoress = (pred[:, :, 0] * 100).astype(int)
            confidence_p = np.divide(confidence_scoress, 100.0)
            overall_confidence = np.max(confidence_p)
            # Assuming binary segmentation
            is_positive = np.any(confidence_scores)
            confidence=0
            if is_positive:
                print("The model predicted the image as positive.")
                axarr.set_title("The model predicted the image as positive.")
                predection = 1
                confidence = overall_confidence*100
            # print("Confidence = ",confidence_scores*100)
            else:
                print("The model predicted the image as negative.")
                axarr.set_title("The model predicted the image as negative.")
                predection = 0
                confidence = 100-overall_confidence*100
            # print("Confidence = ",confidence_scores*100)
            # Optionally, you can print or use these confidence scores as needed
            # print("Confidence Scores:", confidence_scores)
            # apply bounding boxes
            predictionString = ''
            for region in measure.regionprops(comp):
                # retrieve x, y, height and width
                y, x, y2, x2 = region.bbox
                height = y2 - y
                width = x2 - x
                # axarr[axidx].add_patch(patches.Rectangle((x,y),width,height,linewidth=2,edgecolor='r',facecolor='none'))
                axarr.add_patch(patches.Rectangle((x,y),width,height,linewidth=2,edgecolor='b',facecolor='none'))
            # axidx += 1
        img_buffer = io.BytesIO()
        # plt.axes('off')
        plt.gca().set_axis_off()
        plt.savefig(img_buffer, format='png')
        file_path = os.path.join(settings.BASE_DIR,'..\..\Frontend\src\Components\python_preds',image_name)
        plt.savefig(file_path, format='png')
        image = cv2.imread(file_path)

    # Crop the image using NumPy array slicing
        cropped_image = image[140:1370, 415:1635]

    # Save the cropped image
        cv2.imwrite(file_path, cropped_image)
        # plt.show()
        img_buffer.seek(0)
        # response = HttpResponse(content_type='image/png')
        plt.close()
        # return response
        # plt.close()
        # only plot one batch
        break
    return img_buffer, predection, file_path,confidence

def upload(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        # Process the image as needed (e.g., save it to the model)
        # Return a JSON response indicating success or failure
        unique_filename = os.path.join(settings.MEDIA_ROOT, 'downloads', image.name)
        
        with open(unique_filename, 'wb') as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        
        buffer_image, pred, file_path,conf = recieve_preds(image.name)
        buffer_image.seek(0)
        file_name = os.path.basename(file_path)
        
        print(pred)

        return JsonResponse({'pred': pred,'url':file_name,'conf':conf})
    else:
        return JsonResponse({'status': 'error'})
# Create your views here.
