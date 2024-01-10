from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Add the origin of your React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load the pre-trained model
model_path = "../models/model2"
model = tf.keras.models.load_model(model_path)
class_names = ["NORMAL", "PNEUMONIA"]

def preprocess_image(file_contents):
    image = Image.open(BytesIO(file_contents)).convert("RGB")
    image = image.resize((256, 256))
    return np.expand_dims(image, axis=0)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
       
        image = preprocess_image(contents)

        # Make prediction
        prediction = model.predict(image)
        predicted_class_index = np.argmax(prediction)
        predicted_class = class_names[predicted_class_index]
        confidence = float(prediction[0][predicted_class_index])

        return {
            "prediction": predicted_class,
            "confidence": confidence    
        }
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)


