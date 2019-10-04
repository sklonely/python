import cv2
import numpy as np
# import skin_detector


img = cv2.imread('567.jpg')
# 圖片前處理
# image = cv2.resize(img, (256, 256), interpolation=cv2.INTER_CUBIC)
image = img

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (11, 11), 0)

binaryIMG = cv2.Canny(blurred, 20, 100)

(cnts, _) = cv2.findContours(binaryIMG.copy(),
                             cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if len(cnts) == 0:
    print(0)
else:
    # 找出輪廓中最大的，假設為手
    segmented = max(cnts, key=cv2.contourArea)
cv2.drawContours(image, cnts, -1, (0, 255, 0), 2)
cv2.imshow("1", binaryIMG)
cv2.waitKey(0)
