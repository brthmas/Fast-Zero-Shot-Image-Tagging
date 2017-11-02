import numpy as np

#CNN to Classify Image

from keras.applications.vgg19 import VGG19, preprocess_input
from keras.preprocessing import image

img_model = VGG19(include_top=False, pooling="max")

img_path = ""
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

img_features = img_model.predict(x)

#Ranking SVM to create word-association space

import ranking

X_train_words = [] #input tags as word vector
y_train_words = [] #whether or not each tag is relevant to the image
rank_svm = RankSVM().fit()
word_features = rank_svm.predict(X_train_words)

#We approximate the principle direction, w, with a linear regression model

from sklearn.linear_model import LinearRegression

w = LinearRegression().fit(img_features,word_features)
