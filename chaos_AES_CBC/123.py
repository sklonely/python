import cv2
import numpy as np
from matplotlib import pyplot
import math
from AESmod import AEScharp
import time
import multiprocessing
from functools import reduce

aes = AEScharp()


def en_cbc(data, key):
    _16BitList = []
    en_data = b''
    num = 16  #定义每组包含的元素个数

    for i in range(0, len(data), num):
        _16BitList.append(data[i:i + num])

    t = 0
    for i in _16BitList:
        en_data += aes.encrypt_ECB_by(i, t)
        t += 1

    # print(len(en_data))
    return en_data


if __name__ == "__main__":

    try:
        cam = cv2.VideoCapture(0)
        # for i in range(200):
        
        (ret, img) = cam.read()
        # cv2.imshow(u'ORG', img)  # 輸出圖像
        stringData = img.tostring()  # 轉成bytes

        ### [test]
        tt = time.time()
        e_sss = en_cbc(stringData, 2)
        # e_sss = aes.encrypt_ECB_by(stringData, "1")  # 加密
        print('Time used: {} sec'.format(time.time() - tt))

        d_sss = aes.decrypt_ECB_by(e_sss, '1').rstrip()  # 解密

        e_sss = np.fromstring(e_sss, dtype='uint8').reshape(img.shape)  # string to matrix
        d_sss = np.fromstring(d_sss, dtype='uint8').reshape(img.shape)  # string to matrix

        cv2.imshow(u'en', e_sss)  # 輸出圖像
        cv2.imshow(u'de', d_sss)  # 輸出圖像
        cv2.waitKey(0)
    finally:
        cv2.destroyAllWindows()
