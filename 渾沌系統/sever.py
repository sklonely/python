from flask import Flask, jsonify, request
from HENMAP_chaos_model import Chaos
from AESmod import AEScharp
import random
import json
import time
import threading
import hashlib
app = Flask(__name__)
# 變數


@app.route("/")
def hello():
    return str("歡迎來到渾沌加解密測試首頁")


# @app.route("/encrypt", methods=['POST'])
@app.route("/encrypt")
def encrypt():
    temp_Um = Um

    return ("key: " + str(X[0]) + " Um:" + str(temp_Um))


@app.route("/AES_encrypt")
def AES_encrypt(data="你好世界"):
    # 加密資料
    temp_Um = Um
    key = X[0]
    aes = AEScharp()
    sendData = aes.encrypt(data, key)
    global testEN
    testEN = sendData
    # json 黨製作
    sendData = {'密文:': str(sendData), 'Um:': str(temp_Um)}
    return json.dumps(sendData)


@app.route("/decrypt")
def decrypt():
    # 同步key值
    temp_X = X
    temp_Um = Um
    Y = [random.random(), random.random(), random.random()]
    client = Chaos()
    for i in range(19, -1, -1):
        Y = client.runSlave(2, Y, temp_Um[i])
        UK = client.createUk(temp_X, Y)
    print(temp_X[0], Y[0], UK)
    # 解密
    aes = AEScharp()
    getData = aes.decrypt(testEN, Y[0])
    # print(temp_Um)
    return str(getData)


def chaos():
    # 初始化
    sys_chaos = Chaos()
    global X, Um
    X = [-1.3156345, -1.84, 0.5624]
    Um = []
    for i in range(20):
        Um.append(0)
    Um[0] = sys_chaos.createUm(X)
    X = sys_chaos.runMaster(0, X)
    # 進入迴圈開始跑渾沌
    while 1:
        for i in range(19, 0, -1):
            Um[i] = Um[i - 1]
        Um[0] = sys_chaos.createUm(X)
        X = sys_chaos.runMaster(1, X)
        time.sleep(0.1)


if __name__ == "__main__":
    try:
        sys_chaos = threading.Thread(target=chaos)
        sys_chaos.setDaemon(True)
        sys_chaos.start()
        time.sleep(2)
        AES_encrypt()
        for i in range(10):
            time.sleep(1)
            decrypt()
        # app.run()
    except 1:
        print("退出渾沌加密系統")
