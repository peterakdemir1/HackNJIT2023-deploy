from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.models import Model
from keras.models import load_model
import numpy as np

# this is the VGG16 pre-trained model for image classification
# model = VGG16(weights='imagenet')
# model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
# model.save('vgg16-feature-extractor.h5')

model = load_model('vgg16-feature-extractor.h5')

image1 = image.load_img('test-images/laptop2.jpg', target_size=(224,224))
image2 = image.load_img('test-images/laptop4.jpg', target_size=(224,224))
image1 = image.img_to_array(image1)
image2 = image.img_to_array(image2)
image1 = np.expand_dims(image1, axis=0)
image2 = np.expand_dims(image2, axis=0)
image1 = preprocess_input(image1)
image2 = preprocess_input(image2)

# get features through predict
features1 = model.predict(image1)
features2 = model.predict(image2)

similarity = np.dot(features1, features2.T)

cosine_similarity = similarity / (np.linalg.norm(features1) * np.linalg.norm(features2))
print('Cosine Similarity:', cosine_similarity[0][0])
