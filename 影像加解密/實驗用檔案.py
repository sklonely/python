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
pc_flage = 0
X = []  # 混沌亂數
Y = []  # 混沌亂數接收端
Um = 0  # 同步用
img = 0  # 圖片


def chaos():  # 渾沌模組 工作不會同步問題
    # 初始化 準備Um buff
    sys_chaos = Chaos()
    sr_chaos = Chaos()
    global X, Um, pc_flage
    X = [random.random(), random.random(), random.random()]
    # Y = [random.random(), random.random(), random.random()]
    Um = sys_chaos.createUm(X)
    X = sys_chaos.runMaster(0, X)
    # Y = sr_chaos.runSlave(0, Y, Um)
    # 進入迴圈開始跑渾沌
    while 1:
        if pc_flage == 0:
            Um = sys_chaos.createUm(X)
            X = sys_chaos.runMaster(2, X)
            # Y = sr_chaos.runSlave(2, Y, Um)
            pc_flage = 1
        time.sleep(0.0001)
        # print(X)


def chaos_S():  # 渾沌模組
    # 初始化 準備Um buff
    sr_chaos = Chaos()
    global Y, pc_flage
    Y = [random.random(), random.random(), random.random()]
    Y = sr_chaos.runSlave(0, Y, Um)
    # 進入迴圈開始跑渾沌
    while 1:
        if pc_flage == 1:
            Y = sr_chaos.runSlave(2, Y, Um)
            pc_flage = 2
        time.sleep(0.0001)
        # print(X)


def encodeing(vis_o, use_key):  # 圖片加密
    # 變數
    (w, h, a) = vis_o.shape  # 圖片大小
    vis = vis_o.copy()
    # 加密開始
    count = 0
    for _ in range(5):
        for i in range(479):  # 輪廓打亂
            t = use_key[0][count]  # 混沌亂數加入
            if count >= 31:
                count = 0
            else:
                count += 1
            vis[[i, t], :] = vis[[t, i], :]
    # for i in range(479, -1, -1):  # 輪廓打亂
    #     t = use_key[0][count]  # 混沌亂數加入

    #     if count <= 0:
    #         count = 31
    #     else:
    #         count += -1
    #     vis[[i, t], :] = vis[[t, i], :]
    # vis = vis.transpose(1, 0, 2)
    # count = 0
    # for _ in range(5):
    #     for i in range(639):
    #         t = use_key[1][count]  # 混沌亂數加入
    #         if count >= 31:
    #             count = 0
    #         else:
    #             count += 1
    #         vis[[i, t], :] = vis[[t, i], :]
    # vis = vis.transpose(1, 0, 2)
    return vis


def decodeing_colr(vis_o, use_key):
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


def encodeing_colr(vis_o, use_key):
    # 變數
    (w, h, a) = vis_o.shape  # 圖片大小
    vis = vis_o.copy()
    # 加密開始
    count = -1
    for i in range(w):  # 顏色打亂
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


if __name__ == '__main__':
    try:
        # 啟動本機系統的主混沌系統
        sys_chaos = threading.Thread(target=chaos)
        sys_chaos.setDaemon(True)
        sys_chaos.start()
        print("SYS_Chaos主端 初始化完成...")
        sys_chaos = threading.Thread(target=chaos_S)
        sys_chaos.setDaemon(True)
        sys_chaos.start()
        print("SYS_Chaos從端 初始化完成...")
        print("SYS_Chaos 全部初始化完成 進入系統...")
    except 1:
        pass
    # 初始化設定(相機裝置,樸端混沌系統)
    cam = cv2.VideoCapture(0)
    # sr_chaos = Chaos()
    # Y = [random.random(), random.random(), random.random()]
    # Y = sr_chaos.runSlave(0, Y, Um)
    while True:
        # 影像讀取
        # print("E1",round(X[0], 6)-round(Y[0], 6),"E2",round(X[1], 6)-round(Y[1], 6))
        (ret, img) = cam.read()
        vis = img.copy()  # type= <class 'numpy.ndarray'>
        # 同步 and 金鑰產生
        # Y = sr_chaos.runSlave(2, Y, Um)
        if pc_flage == 2:
            key = []
            key.append(list(hashlib.sha256(str(round(X[0], 6)).encode('utf-8')).digest()))
            key.append(list(hashlib.sha256(str(round(X[1], 6)).encode('utf-8')).digest()))
            use_key = []
            use_key.append(list(hashlib.sha256(str(round(Y[0], 6)).encode('utf-8')).digest()))
            use_key.append(list(hashlib.sha256(str(round(Y[1], 6)).encode('utf-8')).digest()))
            print(key[0] == use_key[0], key[1] == use_key[1])
            pc_flage = 0

        # 加解密區塊
        vise = encodeing_colr(vis, key)
        visd = decodeing_colr(vise, use_key)
        # 顯示區塊
        cv2.imshow(u'Original video', vis)
        cv2.imshow(u'encodeing video', vise)
        cv2.imshow(u'decodeing video', visd)
        cv2.waitKey(10)

    cv2.destroyAllWindows()