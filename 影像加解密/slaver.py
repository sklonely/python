#!/usr/bin/python3
# 文件名：client.py

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

Y = [0, 0, 0]
pc_flage = 0
Um = 0
sr_chaos = Chaos()


def chaos_S():  # 渾沌模組
    # 初始化 準備Um buff

    global Y, pc_flage
    Y = [random.random(), random.random(), random.random()]
    Y = sr_chaos.runSlave(0, Y, Um)


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
        while True:  # 資料接收主程式
            # 影像主要資料
            msg = recv_data_sockite()  # 資料接收相對應的大小
            if (len(msg) > 1000):  # 簡單判斷是不是影像
                data = np.fromstring(msg, dtype='uint8')  # 將接收的資料重組成圖片陣列
                data = cv2.imdecode(data, 1)  # 將圖像陣列轉成圖片
            # 金鑰同步
            Um = float(recv_data_sockite().decode('utf-8'))
            Y = sr_chaos.runSlave(2, Y, Um)

            # 解密影像
            key = []
            key.append(list(hashlib.sha256(str(round(Y[0], 6)).encode('utf-8')).digest()))
            key.append(list(hashlib.sha256(str(round(Y[1], 6)).encode('utf-8')).digest()))
            vise = encodeing_colr(data, key)

            # 圖像輸出
            cv2.imshow(u'enconding', data)  # 輸出圖像
            cv2.waitKey(10)
            # DEBUG
            print("除錯用:", Y[0])
    finally:
        cv2.destroyAllWindows()
        s.close()
