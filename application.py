from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import os
from bananagram import bananapi


# curl -X POST -F "file=@/home/moebius/PycharmProjects/Bananagram/bananapics/BLACK_SIGATOKA 0001 124 .jpg" http://localhost:5000/predict

app = Flask(__name__)
api = Api(app)
CORS(app)

class Prediction(Resource):
    def post(self):
        # Get the image from the POST request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file:
            # save the file to disk
            file_path = os.path.join('bananapics', file.filename)
            file.save(file_path)

            # call health_detection function with saved file
            predicted_class = bananapi.health_detection(file_path)

            # return the predicted class as response
            return jsonify({'predicted_class': predicted_class})

api.add_resource(Prediction, '/predict')

if __name__ == '__main__':
    app.run()
