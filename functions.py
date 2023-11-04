from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input
# from keras.models import Model
from keras.models import load_model
import numpy as np
import piexif

# this is the VGG16 pre-trained model for image classification
# model = VGG16(weights='imagenet')
# model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
# model.save('vgg16-feature-extractor.h5')
model = load_model('vgg16-feature-extractor.h5')

# extract image features using vgg16
def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    # get features through predict
    features = model.predict(img)

    return features

# get cosine similarity using image features
def calc_cosine_similarity(features1, features2):
    similarity = np.dot(features1, features2.T)
    cosine_similarity = similarity / (np.linalg.norm(features1) * np.linalg.norm(features2))
    return cosine_similarity[0][0]

# get gps info from image with gps metadata
def get_gps_info(image_path):
    # Load metadata
    exif_dict = piexif.load(image_path)
    # Get the GPS data
    gps_info = exif_dict.get('GPS', {})
    return gps_info

# get latitude and longitude gps info; this takes in gps exif dict as input so use the return value of get_gps_info()
def get_coords(gps_data):
    latitude = {
        'degree': 0,
        'minute': 0,
        'second': 0,
        'reference': 'N'
    }

    longitude = {
        'degree': 0,
        'minute': 0,
        'second': 0,
        'reference': 'W'
    }

    coordinates = [latitude, longitude]

    latitude['degree'] = gps_data[2][0][0] / gps_data[2][0][1]
    latitude['minute'] = gps_data[2][1][0] / gps_data[2][1][1]
    latitude['second'] = gps_data[2][2][0] / gps_data[2][2][1]
    latitude['reference'] = gps_data[1]

    longitude['degree'] = gps_data[4][0][0] / gps_data[4][0][1]
    longitude['minute'] = gps_data[4][1][0] / gps_data[4][1][1]
    longitude['second'] = gps_data[4][2][0] / gps_data[4][2][1]
    longitude['reference'] = gps_data[3]

    return coordinates