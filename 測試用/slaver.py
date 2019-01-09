#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
import socket
import sys
import time
import cv2
import numpy
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
    while True:  # 資料接收主程式
        #獲取資料長度
        lenths = s.recv(6)
        # print(lenths, len(lenths))

        # 確認資料長度格式
        if len(lenths) == 6:
            # ACK相關
            try:
                lenths = int(lenths.decode('utf-8'))
                s.send(b'1')
            except UnicodeDecodeError:
                print("UnicodeDecodeError")
                s.send(b'0')
            # 主要資料
            msg = s.recv(lenths)  # 資料接收相對應的大小
            data = numpy.fromstring(msg, dtype='uint8')  # 將接收的資料重組成圖片陣列
            data = cv2.imdecode(data, 1)  # 將圖像陣列轉成圖片
            cv2.imshow(u'enconding', data)  # 輸出圖像
            cv2.waitKey(10)
        else:  # ACK 相關
            print("data have error")
            s.send(b'0')
finally:
    cv2.destroyAllWindows()
    s.close()
