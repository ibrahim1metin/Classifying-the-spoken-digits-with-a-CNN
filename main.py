import tensorflow as tf
import os
from PIL import Image
import numpy as np
from utils import TrainTestValSplit
X=[]
Y=[]
for i in range(10):
  for file in os.listdir(f"data/{i}/"):
    img=Image.open(f"data/{i}/{file}")
    X.append(np.array(img))
    Y.append(np.array([np.int32(i)]))
X=np.array(X)
Y=np.array(Y)
X=(tf.constant(X))
Y=(tf.constant(Y))
Y=tf.one_hot(Y,10)
Y=tf.squeeze(Y)
Xtrain,Ytrain,Xval,Yval,Xtest,Ytest=(TrainTestValSplit(X,Y,0.1,0.1))
model=tf.keras.Sequential([
  tf.keras.layers.Input(((300,300,4))),
  tf.keras.layers.Conv2D(64,4,activation="relu"),
  tf.keras.layers.BatchNormalization(),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32,(4,4),activation="relu"),
  tf.keras.layers.BatchNormalization(),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(16,activation="relu"),
  tf.keras.layers.Dropout(0.3),
  tf.keras.layers.BatchNormalization(),
  tf.keras.layers.Dense(10),
  tf.keras.layers.Softmax()
])
model.compile(optimizer=tf.keras.optimizers.Adam(0.001),loss=tf.keras.losses.BinaryCrossentropy(),metrics=[tf.keras.metrics.BinaryAccuracy(),tf.keras.metrics.Recall()])
print(model.summary())
model.fit(Xtrain,Ytrain,validation_data=(Xval,Yval),epochs=20,batch_size=128)
model.evaluate(Xtest,Ytest)
