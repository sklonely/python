#import from lib
import cv2
import sys
import os
import random
sys.path.append(sys.path[0] + '/mods/')
from AESmod import AEScharp
import threading
import time
import hashlib
from HENMAP_chaos_model import Chaos
import numpy as np
# local modules
#from video import create_capture
X = []  # 混沌亂數
Um = []  # 同步用
img = 0  # 圖片


def chaos():  # 渾沌模組
    # 初始化 準備Um buff
    sys_chaos = Chaos()
    global X, Um
    X = [random.random(), random.random(), random.random()]
    Um = []
    for i in range(32):
        Um.append(0)
    Um[0] = sys_chaos.createUm(X)
    X = sys_chaos.runMaster(0, X)
    # 進入迴圈開始跑渾沌
    while 1:
        for i in range(31, 0, -1):
            Um[i] = Um[i - 1]
        Um[0] = sys_chaos.createUm(X)
        X = sys_chaos.runMaster(1, X)
        time.sleep(0.001)
        # print(X)


def cath_img():
    global img
    cam = cv2.VideoCapture(0)
    while True:
        (ret, img) = cam.read()
        vis = img.copy()  # type= <class 'numpy.ndarray'>
        (w, h, a) = vis.shape  # (480,640,3)


def encodeing(vis_o, use_key):
    # 圖片加密
    vis = vis_o.copy()
    count = -1
    for i in range(w):
        count += 1
        if count == 32:
            count = 0
        vis[i] += use_key[0][count]
    vis = vis.transpose(1, 0, 2)
    count = 32
    for i in range(h):
        count -= 1
        if count == 1:
            count = 31
        vis[i] += use_key[1][count]
    vis = vis.transpose(1, 0, 2)
    return vis


def decodeing(vis_o, use_key):
    # 圖片解密
    vis = vis_o.copy()
    vis = vis.transpose(1, 0, 2)
    count = 32
    for i in range(h):
        count -= 1
        if count == 1:
            count = 31
        vis[i] -= use_key[1][count]
    vis = vis.transpose(1, 0, 2)
    count = -1
    for i in range(w):
        count += 1
        if count == 32:
            count = 0
        vis[i] -= use_key[0][count]
    return vis


if __name__ == '__main__':
    try:
        # 啟動本機系統的混沌系統
        sys_chaos = threading.Thread(target=chaos)
        sys_chaos.setDaemon(True)
        sys_chaos.start()
        print("SYS_Chaos 初始化完成 進入本機伺服器...")
    except 1:
        pass
    cam = cv2.VideoCapture(0)
    while True:
        # 影像讀取
        (ret, img) = cam.read()
        vis = img.copy()  # type= <class 'numpy.ndarray'>
        (w, h, a) = vis.shape  # (480,640,3)
        # 金鑰產生
        use_key = []
        use_key.append(list(hashlib.sha256(str(X[0]).encode('utf-8')).digest()))
        use_key.append(list(hashlib.sha256(str(X[1]).encode('utf-8')).digest()))
        #加解密區塊
        vise = encodeing(vis, use_key)
        visd = decodeing(vise, use_key)
        #顯示區塊
        cv2.imshow(u'Original video', img)
        cv2.imshow(u'encodeing video', vise)
        cv2.imshow(u'decodeing video', visd)
        cv2.waitKey(10)

    cv2.destroyAllWindows()