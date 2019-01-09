#!/usr/bin/python3
# 文件名：server.py

import hashlib
import os
import random
import socket
import sys
import threading
import time

#import from lib
import cv2
import numpy as np

sys.path.append(sys.path[0] + '/mods/')

from AESmod import AEScharp
from HENMAP_chaos_model import Chaos

# local modules
#from video import create_capture
pc_flage = 0
X = []  # 混沌亂數
Y = []  # 混沌亂數接收端
Um = 0  # 同步用
img = 0  # 圖片

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
port = 9999
# 绑定端口号
serversocket.bind((host, port))
# 设置最大连接数，超过后排队

serversocket.listen(5)


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
    # vis = vis.transpose(1, 0, 2)
    # count = 32
    # for i in range(h):
    #     count -= 1
    #     if count == 1:
    #         count = 31
    #     vis[i] += use_key[1][count]
    # vis = vis.transpose(1, 0, 2)
    return vis


if __name__ == "__main__":

    # 啟動 渾沌系統
    print("SYS_Chaos主端 初始化中...", end="\r")
    sys_chaos = threading.Thread(target=chaos)
    sys_chaos.setDaemon(True)
    sys_chaos.start()
    print("SYS_Chaos主端 初始化完成!")
    print("等待從端連接...")

    # 主程式 影像加密 及 傳輸
    while True:
        try:
            clientsocket, addr = serversocket.accept()
            print("连接成功! 地址: %s" % str(addr))
            cam = cv2.VideoCapture(0)
            while True:
                # 影像讀取
                (ret, img) = cam.read()
                vis = img.copy()  # type= <class 'numpy.ndarray'>

                # 將Um處理成socket可傳輸的形式
                sendUm = str(Um).encode('utf-8')
                print(len(sendUm))
                # 加密影像
                key = []
                key.append(list(hashlib.sha256(str(round(X[0], 6)).encode('utf-8')).digest()))
                key.append(list(hashlib.sha256(str(round(X[1], 6)).encode('utf-8')).digest()))
                vise = encodeing_colr(vis, key)

                # 將影像處理成socket可傳送的形式
                result, imgencode = cv2.imencode('.jpg', vise)  # 圖片編碼
                data = np.array(imgencode)  # 轉成array
                stringData = data.tostring()  # 轉成bytes

                # 傳送影像(BYTES)
                flage = 1
                while (flage):  # 交握失敗重新傳輸
                    clientsocket.send(str(len(stringData)).encode('utf-8').ljust(6))  # 傳送資料長度
                    ack = clientsocket.recv(1)  # ACK 交握接收
                    if ack == b'1':  # ACK 交握
                        flage = 0
                    clientsocket.send(stringData)

                # 顯示原始影像
                cv2.imshow(u'ORG', vis)  # 輸出圖像
                cv2.waitKey(10)

        except:
            break
        finally:
            print("----------------關閉連線----------------")
            cv2.destroyAllWindows()
            clientsocket.close()
