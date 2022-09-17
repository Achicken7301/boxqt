# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 21:28:53 2022

@author: banhb
"""

#importing the necessary modules
from keras.datasets import mnist
import numpy as np

#loading data
(xtrain,ytrain),(xtest,ytest)=mnist.load_data()

#What mnist images look like
import matplotlib.pyplot as plt
print("Training data:")
plt.imshow(xtrain[4])
plt.show()
print("Label of this image is",ytrain[4])

#reshaping data as needed by the model
xtrain=np.reshape(xtrain,(-1,28,28,1))
xtest=np.reshape(xtest,(-1,28,28,1))
xtrain.shape,xtest.shape,ytrain.shape,ytest.shape

#normalising
xtrain=xtrain/255
xtest=xtest/255

#implementing one hot encoding
from keras.utils.np_utils import to_categorical
y_train = to_categorical(ytrain, num_classes=10)
y_test = to_categorical(ytest, num_classes=10)

#importing the model
from keras.models import Sequential

#creating model object
model=Sequential()

#importing layers
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout

#adding layers and forming the model
model.add(Conv2D(32,kernel_size=5,strides=1,padding="Same",activation="relu",input_shape=(28,28,1)))
model.add(MaxPooling2D(padding="same"))

model.add(Conv2D(64,kernel_size=5,strides=1,padding="same",activation="relu"))
model.add(MaxPooling2D(padding="same"))

model.add(Flatten())

# model.add(Dense(1024,activation="relu"))
model.add(Dense(64,activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(10,activation="sigmoid"))

#compiling
model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])

#training the model
# model.fit(xtrain,y_train,batch_size=100,epochs=4,validation_data=(xtest,y_test))
model.fit(xtrain,y_train,batch_size=100,epochs=2,validation_data=(xtest,y_test))

#model train and test scores
model.evaluate(xtrain,y_train),model.evaluate(xtest,y_test)





