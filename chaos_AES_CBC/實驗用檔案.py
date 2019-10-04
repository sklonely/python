import asyncio
import time
import cv2
from AESmod import AEScharp
import multiprocessing as mp

aes = AEScharp()

# 讀圖
img = cv2.imread('im.png')
stringData = img.tostring()


def en_cbc(data, key):
    _16BitList = []
    en_data = b''
    num = 16  #定义每组包含的元素个数

    for i in range(0, len(data), num):
        _16BitList.append(data[i:i + num])

    print(len(_16BitList))
    pool = mp.Pool(processes=4)
    t = 0
    # multi_res = pool.apply_async(aes.encrypt_ECB_by, (_16BitList[0],1))

    multi_res = [pool.apply_async(aes.encrypt_ECB_by, (i, 1)) for i in _16BitList]

    pool.close()
    pool.join()
    for i in multi_res:
        en_data += i.get()

    return en_data


if __name__ == '__main__':
    s = time.time()
    en_cbc(stringData, 1)
    print("us time:", time.time() - s)
