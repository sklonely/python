from flask import Flask, jsonify, request
from HENMAP_chaos_model import Chaos
import time
import threading
import hashlib
app = Flask(__name__)
# 變數


@app.route("/")
def hello():
    return str("歡迎來到渾沌加解密測試首頁")


@app.route("/encrypt")
def encrypt():
    temp_Um = Um
    
    return ("key: " + str(X[0]) + " Um:" + str(temp_Um))


def chaos():
    sys_chaos = Chaos()
    i = 0
    global X
    X = [-1.3156345, -1.84, 0.5624]
    while 1:
        global Um
        Um = sys_chaos.createUm(X)
        X = sys_chaos.runMaster(i, X)
        i += 1
        time.sleep(0.1)


if __name__ == "__main__":
    sys_chaos = threading.Thread(target=chaos)
    sys_chaos.start()
    app.run()
