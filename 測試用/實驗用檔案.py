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
Y = []  # 混沌亂數接收端
Um = 0  # 同步用
img = 0  # 圖片


def chaos():  # 渾沌模組 工作不會同步問題
    # 初始化 準備Um buff
    sys_chaos = Chaos()
    sr_chaos = Chaos()
    global X, Um, Y
    X = [random.random(), random.random(), random.random()]
    Y = [random.random(), random.random(), random.random()]
    Um = sys_chaos.createUm(X)
    X = sys_chaos.runMaster(0, X)
    Y = sr_chaos.runSlave(0, Y, Um)
    # 進入迴圈開始跑渾沌
    while 1:
        Um = sys_chaos.createUm(X)
        X = sys_chaos.runMaster(2, X)
        Y = sr_chaos.runSlave(2, Y, Um)
        # print(X[0] - Y[0])
        time.sleep(0.001)
        # print(X)


def chaos_S():  # 渾沌模組
    # 初始化 準備Um buff
    sr_chaos = Chaos()
    global Y
    Y = [random.random(), random.random(), random.random()]
    Y = sr_chaos.runSlave(0, Y)
    # 進入迴圈開始跑渾沌
    while 1:
        X = sr_chaos.runSlave(2, X, Um)
        time.sleep(0.001)
        # print(X)


def encodeing(vis_o, use_key):
    # 圖片加密
    (w, h, a) = vis_o.shape  # 圖片大小
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
    # for i in range(479):
    #     t = random.randint(0, 479)
    #     temp = vis[i]
    #     vis[i] = vis[t]
    #     vis[t] = temp
    # vis = vis.transpose(1, 0, 2)
    # for i in range(639):
    #     t = random.randint(0, 639)
    #     temp = vis[i]
    #     vis[i] = vis[t]
    #     vis[t] = temp
    # vis = vis.transpose(1, 0, 2)
    return vis


def decodeing(vis_o, use_key):
    # 圖片解密
    (w, h, a) = vis_o.shape  # 圖片大小
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
    # 初始化設定(相機裝置,樸端混沌系統)
    cam = cv2.VideoCapture(0)
    # sr_chaos = Chaos()
    # Y = [random.random(), random.random(), random.random()]
    # Y = sr_chaos.runSlave(0, Y, Um)
    while True:
        # 影像讀取
        (ret, img) = cam.read()
        vis = img.copy()  # type= <class 'numpy.ndarray'>
        # for i in range(479):
        #     t = random.randint(0, 479)
        #     temp = vis[i]
        #     vis[i] = vis[t]
        #     vis[t] = temp
        # vis = vis.transpose(1, 0, 2)
        # for i in range(639):
        #     t = random.randint(0, 639)
        #     temp = vis[i]
        #     vis[i] = vis[t]
        #     vis[t] = temp
        # vis = vis.transpose(1, 0, 2)
        # 同步 and 金鑰產生
        # Y = sr_chaos.runSlave(2, Y, Um)
        key = []
        key.append(list(hashlib.sha256(str(round(X[0], 6)).encode('utf-8')).digest()))
        key.append(list(hashlib.sha256(str(round(X[1], 6)).encode('utf-8')).digest()))
        # use_key = []
        # use_key.append(list(hashlib.sha256(str(round(Y[0], 6)).encode('utf-8')).digest()))
        # use_key.append(list(hashlib.sha256(str(round(Y[1], 6)).encode('utf-8')).digest()))
        # print(key[0] == use_key[0], key[1] == use_key[1])
        # 加解密區塊
        vise = encodeing(vis, key)
        # visd = decodeing(vise, use_key)
        # 顯示區塊
        cv2.imshow(u'Original video', vis)
        cv2.imshow(u'encodeing video', vise)
        # cv2.imshow(u'decodeing video', visd)
        cv2.waitKey(10)

    cv2.destroyAllWindows()