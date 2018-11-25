import numpy as np
import cv2
import sys
import os
import random
sys.path.append(sys.path[0] + '/mods/')
from AESmod import AEScharp
import threading
import time
from HENMAP_chaos_model import Chaos


def chaos():
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
        # print(X)
        time.sleep(0.001)


def random_sample_f32(size=None):
    f32max = 1 << np.finfo(np.float32).nmant
    sample = np.empty(size, dtype=np.float32)
    sample[...] = np.random.randint(0, f32max, size=size) / np.float32(f32max)
    if size is None:
        sample = sample[()]
    return sample


if __name__ == '__main__':
    try:
        # 啟動本機系統的混沌系統
        sys_chaos = threading.Thread(target=chaos)
        sys_chaos.setDaemon(True)
        sys_chaos.start()
        print("SYS_Chaos 初始化完成 進入本機伺服器...")

    except:
        pass

    print(np.float32(123))
