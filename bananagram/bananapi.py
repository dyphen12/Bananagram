import tensorflow as tf
import numpy as np

# Test model load

batch_size = 32
img_height = 180
img_width = 180

class_names = ['BacterialSoftRot', 'BananaAphids', 'BananaBeetle', 'BlackSigatoka', 'Foc', 'Healthy', 'PeudostemWeevil', 'YellowSigatoka']


savemodel = tf.keras.models.load_model('bananagram/bananamodel/Bananagram.h5')


def health_detection(file):

    # Load the image you want to make a prediction on
    img = tf.keras.preprocessing.image.load_img(
        file, target_size=(img_height, img_width)
    )

    # Convert the image to a numpy array
    img_array = tf.keras.preprocessing.image.img_to_array(img)

    # Reshape the array to match the expected input shape of your model
    img_array = tf.expand_dims(img_array, 0)

    # Make a prediction on the image
    predictions = savemodel.predict(img_array)

    # Get the predicted class
    predicted_class = class_names[np.argmax(predictions)]
    print(predicted_class)
    return predicted_class