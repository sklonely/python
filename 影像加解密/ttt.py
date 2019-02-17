#!/usr/bin/python3
# 文件名：server.py

# 导入 socket、sys 模块
import socket
import sys
import cv2
import time
import numpy

cam = cv2.VideoCapture(0)
(ret, img) = cam.read()
vis = img.copy()  # type= <class 'numpy.ndarray'>
result, imgencode = cv2.imencode('.jpg', img)
data = numpy.array(imgencode)
stringData = data.tostring()
print(len(img[0][0]))
data = numpy.fromstring(stringData, dtype='uint8')
data = cv2.imdecode(data, 1)
print(len(data[0][0]))