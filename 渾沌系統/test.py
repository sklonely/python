from HENMAP_chaos_model import Chaos
from env import AEScharp
X = [-1.3156345, -1.84, 0.5624]
Y = [1.7, -1.2, 1.212345]
aes = AEScharp()

Um = 0
Us = 0

sendData = ''
getData = ''

impData = 'sklonely-加密測試系統 V:1.0 測試中ing'

errorCount = 0
succsCount = 0
syncCount = 0

a = Chaos()
b = Chaos()


def show_data(X, Y, Um, Us, UK, sendData, getData):
    print("Um:", round(Um, 4), "Us:", round(Us, 4), "Uk:", round(UK, 4))
    print("X[" + str(i + 1) + "]", X[0])
    print("Y[" + str(i + 1) + "]", Y[0])
    if (UK == 0):
        print("======同步完成======")
        print("密文:  ", sendData)
        print("解密文:  ", getData)
    print("----------------------------------------------")


for i in range(15):
    UK = a.createUk(X, Y)
    Um = a.createUm(X)
    X = a.runMaster(i, X)
    sendData = aes.encrypt(impData, X[0])

    Us = b.createUs(Y)
    Y = b.runSlave(i, Y, Um)
    getData = aes.decrypt(sendData, Y[0])
    # show data
    show_data(X, Y, Um, Us, UK, sendData, getData)
# a.show()
