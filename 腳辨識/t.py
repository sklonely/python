import cv2
import numpy as np
import skin_detector


# 讀圖
img = cv2.imread('tt.jpg')
# 圖片前處理
img = cv2.resize(img, (256, 256), interpolation=cv2.INTER_CUBIC)
# gray = cv2.cvtColor(img,)
mask = skin_detector.crcb_range_sceening(img)


canny = cv2.Canny(mask, 0, 0)

cnts = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)

print(len(cnts))
if len(cnts) == 0:
    print(0)
else:
    # 找出輪廓中最大的，假設為手
    segmented = max(cnts, key=cv2.contourArea)

print(cnts[0][2])
cv2.drawContours(mask, segmented, -1, (0, 255, 0), 2)
cv2.imshow("1", mask)
cv2.waitKey(0)
