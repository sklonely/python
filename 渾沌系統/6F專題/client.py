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


@app.route("/decrypt")
def decrypt(data='8', Um=0):
    # 同步key值
    temp_Um = Um
    Y = [random.random(), random.random(), random.random()]
    client = Chaos()
    for i in range(15, -1, -1):
        Y = client.runSlave(2, Y, temp_Um[i])
        if (client.createUs(Y) == temp_Um[i]):
            pass
    # 解密
    aes = AEScharp()
    getData = aes.decrypt(data, Y[0])
    return str(getData)


def show():
    # 測試寒士
    time.sleep(.5)
    times = 10
    x = 0
    for i in range(times):
        AES_encrypt()
        time.sleep(.05)
        if (decrypt()[1]):
            x += 1
            print(i)
        else:
            print("error", i)
    print("成功:", x, "失敗:", times - x, "同步率:", (x / times) * 100, "%")


if __name__ == "__main__":
    try:
        # 啟動本機系統的混沌系統
        sys_chaos = threading.Thread(target=chaos)
        sys_chaos.setDaemon(True)
        sys_chaos.start()
        print("SYS_Chaos 初始化完成 進入本機伺服器...")
        #show()
        AES_encrypt()
        app.run()
    except 1:
        print("退出渾沌加密系統")
