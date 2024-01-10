from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import io

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (during development)

# Specify the folder where uploaded images will be stored
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello():
    return 'Hello, Flask is up and running!'

@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if the POST request has a file part
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['image']

    # If the user submits an empty form, the file will be empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the uploaded file to the specified folder
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    

    # Check the content type of the request
    if file.content_type.startswith('image'):
        # If it's an image, return the image
        return send_file(file_path, mimetype=file.content_type)
    elif file.content_type.startswith('application/json'):
        # If it's JSON, you can process it and return a response
        json_data = request.json  # Assuming the JSON data is sent in the request body
        # Process the JSON data and return a response
        return jsonify({'message': 'JSON received successfully'})
    else:
        # Handle other content types as needed
        return jsonify({'error': 'Unsupported content type'})

if __name__ == '__main__':
    app.run(debug=True)
