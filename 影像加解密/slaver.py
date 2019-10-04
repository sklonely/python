#!/usr/bin/python3
# 文件名：client.py

from mods.HENMAP_chaos_model import Chaos
from mods.AESmod import AEScharp
import hashlib
import os
import random
import socket
import sys
import threading
import time

# import from lib
import cv2
import numpy as np

Y = [0, 0, 0]
pc_flage = 0
Um = 0
sr_chaos = Chaos()


def chaos_S():  # 渾沌模組
    # 初始化 準備Um buff

    global Y, pc_flage
    Y = [random.random(), random.random(), random.random()]
    Y = sr_chaos.runSlave(0, Y, Um)


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


def recv_data_sockite():
    flage = 1
    while (flage):
        lenths = s.recv(6)
        # 確認資料長度格式
        if len(lenths) == 6:
            # ACK相關
            try:
                lenths = int(lenths.decode('utf-8'))
                s.send(b'1')
                flage = 0
                return s.recv(lenths)  # 資料接收相對應的大小
            except UnicodeDecodeError:
                print("UnicodeDecodeError")
                s.send(b'0')
        else:  # ACK 相關
            print("data have error")
            s.send(b'0')


def send_data_socket(data):
    flage = 1
    while (flage):  # 交握失敗重新傳輸
        s.send(str(len(data)).encode('utf-8').ljust(6))  # 傳送資料長度
        ack = s.recv(1)  # ACK 交握接收
        if ack == b'1':  # ACK 交握
            flage = 0
        s.send(data)


if __name__ == "__main__":

    # 创建 socket 对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 获取本地主机名
    host = socket.gethostname()

    # 设置端口号
    port = 9999

    # 连接服务，指定主机和端口
    s.connect((host, port))

    # 接收主端影像資料
    try:
        chaos_S()
        tt = 0
        while True:  # 資料接收主程式

            # 影像主要資料
            msg = recv_data_sockite()  # 資料接收相對應的大小
            print(msg[200:230])
            data = np.fromstring(msg, dtype='uint8')  # 將接收的資料重組成圖片陣列
            data = cv2.imdecode(data, 1)  # 將圖像陣列轉成圖片

            # 解密影像
            key = []

            print("除錯用:", Y[0], tt)
            key.append(list(hashlib.sha256(str(round(Y[0], 6)).encode('utf-8')).digest()))
            key.append(list(hashlib.sha256(str(round(Y[1], 6)).encode('utf-8')).digest()))
            vise = decodeing_colr(data, key)  # 解密影像

            # 金鑰同步
            Um = float(recv_data_sockite().decode('utf-8'))
            Y = sr_chaos.runSlave(2, Y, Um)

            # 圖像輸出
            cv2.imshow(u'enconding', data)  # 輸出圖像
            cv2.imshow(u'deconding', vise)
            cv2.waitKey(10)
            # DEBUG

            tt += 1
    finally:
        cv2.destroyAllWindows()
        s.close()
