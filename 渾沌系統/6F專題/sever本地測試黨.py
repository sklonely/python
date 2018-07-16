# import自動修復 程式碼片段Stste
lestModName = ""
while 1:
    try:
        import sys
        import os
        sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
        # 要import的東西放這下面
        from flask import Flask, jsonify, request
        from HENMAP_chaos_model import Chaos
        from AESmod import AEScharp
        import random
        import json
        import time
        import threading
        import copy
        import hashlib
    except (ModuleNotFoundError, ImportError):  # python import error
        err = str(sys.exc_info()[1])[17:-1]
        if (lestModName != err):
            print("缺少mod: " + err + " 正在嘗試進行安裝")
            os.system("pip install " + err)
            lestModName = err
        else:
            print("無法修復import問題 請人工檢查", "mod name: " + err)
            sys.exit()
    else:
        del lestModName
        break
# import自動修復 程式碼片段
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


@app.route("/AES_encrypt", methods=['POST'])
def AES_encrypt(data="我愛pyton"):
    # 加密資料
    global sy, ss
    temp_Um = copy.deepcopy(Um)
    key = copy.deepcopy(X[0])
    sy = key
    ss = temp_Um
    aes = AEScharp()
    try:
        data = request.form['data']
    except:
        pass
    sendData = aes.encrypt(data, key)
    global testEN
    testEN = sendData
    for i in sendData:
        print(i)
    print(sendData)
    # json 黨製作
    print(type(sendData))
    #print(int(sendData, 16))
    sendData = {'密文:': str(sendData), 'Um:': str(temp_Um)}
    return json.dumps(sendData)


@app.route("/AES_decrypt")
def decrypt(data='8', Um=0):
    # 同步key值
    temp_X = sy  # 需替換
    temp_Um = ss  # 需替換
    # 開始同步
    async_flag = False
    times = 0
    while async_flag is False:

        Y = [random.random(), random.random(), random.random()]
        client = Chaos()
        chck = 0.99
        for i in range(5, -1, -1):
            Y = client.runSlave(2, Y, temp_Um[i])
            if i == 1:
                chck = client.createUs(Y)

        # 判斷有沒有同步
        if temp_Um[0] + chck:
            # print(temp_X, Y[0], client.createUs(Y), temp_Um[0] + chck)
            async_flag = False
            if times > 12:
                break
            times += 1

        else:
            async_flag = True

    # 解密
    aes = AEScharp()
    getData = aes.decrypt(testEN, Y[0])
    print(str(getData))
    return str(getData), async_flag


def chaos():
    # 初始化 準備Um buff
    sys_chaos = Chaos()
    global X, Um
    X = [random.random(), random.random(), random.random()]
    Um = []
    for i in range(50):
        Um.append(0)
    Um[0] = sys_chaos.createUm(X)
    X = sys_chaos.runMaster(0, X)
    # 進入迴圈開始跑渾沌
    while 1:
        for i in range(49, 0, -1):
            Um[i] = Um[i - 1]
        Um[0] = sys_chaos.createUm(X)
        X = sys_chaos.runMaster(1, X)
        # print(X[0], Um[0])
        time.sleep(0.001)


def show(times=50):
    # 測試寒士
    time.sleep(.2)
    x = 0
    for i in range(times):
        AES_encrypt()
        time.sleep(.05)
        if (decrypt()[1]):
            x += 1
            print(i, True)
        else:
            print(i, False)
    print("成功:", x, "失敗:", times - x, "同步率:", (x / times) * 100, "%")


if __name__ == "__main__":
    try:
        # 啟動本機系統的混沌系統
        sys_chaos = threading.Thread(target=chaos)
        sys_chaos.setDaemon(True)
        sys_chaos.start()
        print("SYS_Chaos 初始化完成 進入本機伺服器...")
        show()
        # AES_encrypt()
        # app.run()
    except 1:
        print("退出渾沌加密系統")
