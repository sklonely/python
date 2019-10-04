import math

import cv2
import imutils
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pyautogui
from keras import models
from keras.callbacks import TensorBoard
from keras.layers import Convolution2D, Dense, Dropout, Flatten, MaxPool2D
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator


# global variables
bg = None

# 前後景分離用


def run_avg(image, aWeight):
    global bg
    # 初始化背景
    if bg is None:
        bg = image.copy().astype("float")
        return

    # 更新背景(影像,背景,更新速度)
    cv2.accumulateWeighted(image, bg, aWeight)


# ---------------------------------------------
# 手位置辨識
# ---------------------------------------------


def segment(image, threshold=25):
    global bg
    # 找出背景與主體差
    diff = cv2.absdiff(bg.astype("uint8"), image)

    # 閾值差異圖像，以便我們得到前景
    thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]

    # 獲得閾值圖像中的輪廓
    (cnts, _) = cv2.findContours(thresholded.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 沒輪廓就表示沒手
    if len(cnts) == 0:
        return
    else:
        # 找出輪廓中最大的，假設為手
        segmented = max(cnts, key=cv2.contourArea)
        return (thresholded, segmented)


def get_defects(cnt, drawing):
    defects = None
    hull = cv2.convexHull(cnt)
    hull = cv2.convexHull(cnt, returnPoints=False)       # For finding defects
    if hull.size > 15:
        defects = cv2.convexityDefects(cnt, hull)
    return defects

# Gesture Recognition


def keras_process_image(img):
    img = cv2.resize(img, (128, 128))
    img = np.array(img, dtype=np.float32)
    img = np.reshape(img, (1, 128, 128, 1))

    return img/255


def put_prey(pre_y, label):
    output = "None"

    for i in range(len(pre_y[0])):
        if pre_y[0][i] == max(pre_y[0]):
            # print("true", pre_y[0][i], i)
            output = label[i]

    return output


def move(last, now):
    print(now[0][0] - last[0][0])
    return 0


# -----------------
# MAIN FUNCTION
# -----------------
if __name__ == "__main__":

    train_pic_gen = ImageDataGenerator(rescale=1./255, rotation_range=20, width_shift_range=0.2, height_shift_range=0.2,
                                       shear_range=0.2, zoom_range=0.5, horizontal_flip=True, fill_mode='nearest')
    model = models.load_model('cnn_model.h5')
    # 初始化權重
    aWeight = 0.5

    # 初始化攝影機
    camera = cv2.VideoCapture(0)

    # ROI設定
    top, right, bottom, left = 70, 450, 285, 690

    # 背景用的初始化
    num_frames = 0

    while(True):
        # 讀影像
        (grabbed, frame) = camera.read()

        # 調整畫面大小
        frame = imutils.resize(frame, width=700)

        # 翻轉影像
        frame = cv2.flip(frame, 1)

        # 複製處理用的影像
        clone = frame.copy()

        # 獲取原影像的型態 (長寬)
        (height, width) = frame.shape[:2]

        # 抓取roi區域
        roi = frame[top:bottom, right:left]

        # 轉換到GRAY下做高斯
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)

        # 更新背景
        if num_frames < 50:
            run_avg(gray, aWeight)
            # 初始幀數+1
            num_frames += 1
            num = 0
            cv2.putText(
                clone, "reset bg plase wait...", (0, 30), 0, 1, (0, 0, 255))
            last = gray
        else:
            # 找手
            hand = segment(gray)
            model
            # 檢查手區域是否存在
            if hand is not None:
                # 分割區域
                (thresholded, segmented) = hand

                if cv2.contourArea(segmented) >= 2500:
                    a = keras_process_image(thresholded)
                    move(last, segmented)
                    last = segmented
                    pre_y = model.predict(a)
                    output = put_prey(
                        pre_y, ["zero", "one", "two", "three", "four", "five"])

                    cv2.putText(clone, output, (0, 30), 0, 1, (0, 0, 255))
                    # 凸點與凹點比較找出手型
                    if thresholded is None:
                        num += 1
                        if num > 50:
                            num_frames = 0
                    else:
                        num = 0
                    cv2.imshow("Thesholded", thresholded)

        # 畫辨識區
        cv2.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)

        cv2.imshow("Video Feed", clone)

        keypress = cv2.waitKey(1) & 0xFF

        # if the user pressed "q", then stop looping
        if keypress == ord("q"):
            break
        if keypress == ord("r"):
            num_frames = 0

# free up memory
camera.release()
cv2.destroyAllWindows()
