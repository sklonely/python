import asyncio
import time
import cv2
import numpy as np
from AESmod import AEScharp
from functools import reduce
import struct
import multiprocessing as mp
from HENMAP_chaos_model import Chaos
from numba import jit, autojit
import random

X = [0.12345, 0.23456, 0.34567]
Y = [0.222222, 0.111111, 0.333333]
a = Chaos()
b = Chaos()
aes = AEScharp()

# 讀圖
img = cv2.imread('im.png')
stringData = img.tostring()


def en_cbc(data):
    global X
    minx = X
    _16BitList = []
    key = []
    en_data = b''
    num = 16  #定義每组包含的元素個数

    for i in range(0, len(data), num):
        _16BitList.append(data[i:i + num])

    en = aes.encrypt_ECB_by

    for i in _16BitList:
        minx = a.runMaster(2, minx)
        key.append(minx[0])

    t = map(en, _16BitList, key)
    en_data = reduce(lambda x, y: x + y, list(t))

    X = minx
    return en_data, key


def de_cbc(data, key):
    _16BitList = []
    de_data = b''
    num = 16  #定义每组包含的元素个数

    for i in range(0, len(data), num):
        _16BitList.append(data[i:i + num])

    t = 0
    de = aes.decrypt_ECB_by
    for i in _16BitList:
        de_data += de(i, key[t])
        t += 1

    return de_data


if __name__ == '__main__':
    file_bitarray = b''
    for i in range(1):
        s = time.time()
        (e_sss, key) = en_cbc(stringData)
        # e_sss = aes.encrypt_CBC_speed(stringData, 1)
        print("us time:", time.time() - s)
        temp = e_sss
        file_bitarray += temp
        e_sss = np.frombuffer(e_sss, dtype='uint8').reshape(img.shape)  # string to matrix

        # d_sss = de_cbc(temp, key)
        # d_sss = np.frombuffer(d_sss, dtype='uint8').reshape(img.shape)
        cv2.imshow(u'org', img)
        cv2.imshow(u'en', e_sss)  # 輸出圖像
        cv2.waitKey(0)
    print(len(file_bitarray))
    with open('data.bin', 'wb') as f:
        f.write(file_bitarray)
