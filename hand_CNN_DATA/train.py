from keras.models import Sequential
from keras.layers import Convolution2D, MaxPool2D, Flatten, Dense, Dropout
from keras.callbacks import TensorBoard
from keras.preprocessing.image import ImageDataGenerator

from keras import models
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
from glob import glob

train_dir = ("train")

test_dir = ("test")

train_pic_gen = ImageDataGenerator(rescale=1. / 255, rotation_range=20, width_shift_range=0.2, height_shift_range=0.2, shear_range=0.2, zoom_range=0.5, horizontal_flip=True, fill_mode='nearest')

test_pic_gen = ImageDataGenerator(rescale=1. / 255)

train_flow = train_pic_gen.flow_from_directory(train_dir, (128, 128), batch_size=32, class_mode='categorical', color_mode='grayscale')

test_flow = test_pic_gen.flow_from_directory(test_dir, (128, 128), batch_size=32, class_mode='categorical', color_mode='grayscale')


def get_num_of_classes():
    return len(glob('train/*'))


# 訓練
model = Sequential([
    Convolution2D(32, 3, 3, input_shape=(128, 128, 1), activation='relu'),
    MaxPool2D(pool_size=(2, 2)),
    Convolution2D(64, 3, 3, input_shape=(128, 128, 1), activation='relu'),
    MaxPool2D(pool_size=(2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dropout(0.5),
    # Dense(64,activation='relu'),
    Dense(6, activation='softmax')
])

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='nadam', metrics=['accuracy'])

model = models.load_model('cnn_model.h5')

model.fit_generator(train_flow, steps_per_epoch=100, epochs=50, verbose=1, validation_data=test_flow, validation_steps=100, callbacks=[TensorBoard(log_dir='./logs/1')])

model.save('cnn_model.h5')
