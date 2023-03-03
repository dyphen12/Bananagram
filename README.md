# Bananagram

Bananagram is a machine learning model built with TensorFlow to classify 
images of bananas based on their health status. 
It can detect the following banana health conditions: 
Bacterial Soft Rot, Banana Aphids, Banana Beetle, Black Sigatoka, Fusarium Wilt, 
Healthy, Pseudostem Weevil, and Yellow Sigatoka.

## Usage

To use Bananagram, you can send a POST request 
to the /predict endpoint of the API with an 
image file in the request body. 
The API will return the predicted 
class of the image based on its health status.


`
curl -X POST -F "file=@/path/to/image.jpg" http://localhost:5000/predict
`

## Installation
1. Clone the Bananagram repository:

`git clone https://github.com/your_username/bananagram.git
`
2. Create and activate a virtual environment:

`python3 -m venv venv`

`source venv/bin/activate`

3. Install the required packages:

`pip install -r requirements.txt`

4. Start the Flask server:

`export FLASK_APP=app.py`

`flask run`


### Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

### License
Bananagram is licensed under the MIT License.