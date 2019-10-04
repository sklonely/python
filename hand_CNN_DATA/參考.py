from keras.models import Sequential
from keras.layers import Convolution2D, MaxPool2D, Flatten, Dense, Dropout
from keras.callbacks import TensorBoard
from keras.preprocessing.image import ImageDataGenerator

from keras import models
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

train_dir = ("train")

test_dir = ("test")

train_pic_gen = ImageDataGenerator(rescale=1./255, rotation_range=20, width_shift_range=0.2, height_shift_range=0.2,
                                   shear_range=0.2, zoom_range=0.5, horizontal_flip=True, fill_mode='nearest')

test_pic_gen = ImageDataGenerator(rescale=1./255)


train_flow = train_pic_gen.flow_from_directory(
    train_dir, (128, 128), batch_size=32, class_mode='categorical')

test_flow = test_pic_gen.flow_from_directory(
    test_dir, (128, 128), batch_size=32, class_mode='categorical')

lena = mpimg.imread('dog.113.jpg')



def get_inputs(src=[]):
    pre_x = []
    for s in src:
        input = cv2.imread(s)
        input = cv2.resize(input, (128, 128))
        input = cv2.cvtColor(input, cv2.COLOR_BGR2RGB)
        pre_x.append(input)
    pre_x = np.array(pre_x) / 255.0
    return pre_x


print(get_inputs(['dog.113.jpg']))


def put_prey(pre_y, label):
    output = []
    for y in pre_y:
        if y[0] < 0.5:
            output.append([label[0], 1-y[0]])
        else:
            output.append([label[1], y[0]])
    return output


model = models.load_model('catdogs_model.h5')

pre_x = get_inputs(['dog.113.jpg'])

plt.imshow(lena)
pre_y = model.predict(pre_x)
print(pre_y)
output = put_prey(pre_y, list(train_flow.class_indices.keys()))
print(output)
plt.show()

# # 訓練
# model = Sequential([
#     Convolution2D(32, 3, 3, input_shape=(128, 128, 3), activation='relu'),
#     MaxPool2D(pool_size=(2, 2)),
#     Convolution2D(64, 3, 3, input_shape=(128, 128, 3), activation='relu'),
#     MaxPool2D(pool_size=(2, 2)),
#     Flatten(),
#     Dense(64, activation='relu'),
#     Dropout(0.5),
#     # Dense(64,activation='relu'),
#     Dense(2, activation='softmax')


# ])

# model.summary()

# model.compile(loss='categorical_crossentropy',
#               optimizer='nadam', metrics=['accuracy'])

# model.fit_generator(
#     train_flow, steps_per_epoch=100, epochs=50, verbose=1, validation_data=test_flow, validation_steps=100,
#     callbacks=[TensorBoard(log_dir='./logs/1')]
# )

# model.save('catdogs_model.h5')
