# -*- coding:utf-8 -*-
import cv2
import numpy as np


def ellipse_detect(image):
    """YCrCb颜色空间的椭圆肤色分割"""
    # image = cv2.imread(image, cv2.IMREAD_COLOR)
    skinCrCbHist = np.zeros((256, 256), dtype=np.uint8)
    cv2.ellipse(skinCrCbHist, (113, 155), (23, 15),
                43, 0, 360, (255, 255, 255), -1)
    YCRCB = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
    (y, cr, cb) = cv2.split(YCRCB)
    mask = np.zeros(cr.shape, dtype=np.uint8)
    (x, y) = cr.shape
    for i in range(0, x):
        for j in range(0, y):
            CR = YCRCB[i, j, 1]
            CB = YCRCB[i, j, 2]
            if skinCrCbHist[CR, CB] > 0:
                mask[i, j] = 255
    return mask


def cr_otsu(image):
    """YCrCb颜色空间的Cr分量+Otsu阈值分割"""
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
    (y, cr, cb) = cv2.split(ycrcb)
    cr = cv2.GaussianBlur(cr, (5, 5), 0)
    cv2.imshow("cr", cr)
    gry = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cr1 = cv2.GaussianBlur(gry, (5, 5), 0)
    _, mask = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return mask


def crcb_range_sceening(image):
    """YCrCb颜色空间的CrCb分量阈值分割"""
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
    (y, cr, cb) = cv2.split(ycrcb)
    mask = np.zeros(cr.shape, dtype=np.uint8)
    (x, y) = cr.shape
    for i in range(0, x):
        for j in range(0, y):
            if (cr[i][j] > 140) and (cr[i][j]) < 175 and (cb[i][j] > 100) and (cb[i][j]) < 120:
                mask[i][j] = 255
            else:
                mask[i][j] = 0
    return mask


def hsv_detect(image):
    """HSV颜色空间的阈值分割"""
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    (_h, _s, _v) = cv2.split(hsv)
    mask = np.zeros(_h.shape, dtype=np.uint8)
    (x, y) = _h.shape
    for i in range(0, x):
        for j in range(0, y):
            if (_h[i][j] > 7) and (_h[i][j] < 20) and (_s[i][j] > 28) and (_s[i][j] < 255) and (_v[i][j] > 50) and (
                    _v[i][j] < 255):
                mask[i][j] = 255
            else:
                mask[i][j] = 0

    return mask


img = cv2.imread('567.jpg')
# 圖片前處理
image = cv2.resize(img, (256, 256), interpolation=cv2.INTER_CUBIC)

if __name__ == "__main__":
    
    # cv2.imshow("1", ellipse_detect(image))
    cv2.imshow("2", cr_otsu(image))
    # cv2.imshow("3", crcb_range_sceening(image))
    # cv2.imshow("4", hsv_detect(image))
    cv2.waitKey(0)
