import cv2
import numpy as np
import skin_detector

# cnt = contours  # 取第一条轮廓
# for i in cnt:
#     M = cv2.moments(cnt)  # 计算第一条轮廓的矩
#     print(M)


# rr(cnt, imgnew)
# cx = int(M['m10']/M['m00'])
# cy = int(M['m01']/M['m00'])
# cv2.drawMarker(imgnew, (cx, cy), (0, 255, 0))
# # print(M)
# cv2.imshow("1", imgnew)
# cv2.waitKey(0)

# 讀圖
img = cv2.imread('tt.jpg')
# 圖片前處理
img = cv2.resize(img, (256, 256), interpolation=cv2.INTER_CUBIC)
# 膚色二值化
mask = skin_detector.process(img, 0.6)
cv2.imshow("1", mask)
cv2.waitKey(0)
# # 尋找最大面積

# # M計算中點

