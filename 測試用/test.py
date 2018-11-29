import sys
import os
sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
from AESmod import AEScharp
import hashlib
from HENMAP_chaos_model import Chaos
import random
import time
X = [-1.3156345, -1.84, 0.5624]
aes = AEScharp()

Um = 0
Us = 0

sendData = ''
getData = ''

impData = 'sklonley-AES test'
errorCount = 0
succsCount = 0
syncCount = 0

a = Chaos()
b = Chaos()


def show_data(X, Y, Um, Us, UK, sendData, getData, j):
    print("Um:", round(Um, 4), "Us:", round(Us, 4), "Uk:", round(UK, 4))
    print("X[" + str(j + 1) + "]", X[2])
    print("Y[" + str(j + 1) + "]", Y[2])
    if (UK == 0):
        print("======同步完成======")
        print("bytes: ", sendData.hex())
        print("org", sendData)
        """
        print("sss", bytes.fromhex(sendData.hex()))
        
        
        temp =""
        for i in sendData:
            temp +=hex(i)[2:]
        print(temp)
        """
        print("密文:  ", str(sendData, encoding='utf-8', errors="ignore"))
        #　print("密文做utf8回來 bytes: ", str(sendData, encoding='utf-8', errors="ignore").encode("utf-8"))
        print("解密文:  ", getData)
        return True
    print("----------------", j, "----------------")


tryy = 10
times = 0.0
MaxTimes = 0

for j in range(tryy):
    Y = [random.random(), random.random(), random.random()]
    for i in range(10000):
        UK = a.createUk(X, Y)
        Um = a.createUm(X)
        X = a.runMaster(i, X)
        sendData = aes.encrypt_ECB(impData, X[0])
        # print(int(impData.encode('utf-8')))
        Y = b.runSlave(i, Y, Um)
        getData = aes.decrypt_ECB(bytes.fromhex(sendData.hex()), Y[0])
        if (show_data(X, Y, Um, Us, UK, sendData, getData, j)):
            print("----------------------------------------------")
            print("同步所需次數", i + 1)
            if (MaxTimes <= i):
                MaxTimes = i
            times += (i + 1)
            break
print("平均同步次數:", times / tryy, "最大次數:", MaxTimes)

# # a.show()
# def conv(text, lenth):
#     new_text = []
#     li = 0
#     maxl = len(text)
#     i = 0

#     for i in range(lenth, maxl + 1, lenth):
#         new_text.append(text[li:i])
#         li = i

#     if i != maxl:
#         text = text[i:]
#         for j in range(lenth - (maxl - i)):
#             text += b" "
#         new_text.append(text)
#     return new_text

# """
# """
# """
# def pad_len():
#     def conv(text, lenth):
#         new_text = []
#         li = 0
#         maxl = len(text)
#         i = 0

#         for i in range(lenth, maxl + 1, lenth):
#             new_text.append(text[li:i])
#             li = i

#         if i != maxl:
#             text = text[i:]
#             for j in range(lenth - (maxl - i)):
#                 text += b" "
#             new_text.append(text)
#         return new_text

#     # Y = [random.random(), random.random(), random.random()]
#     text = "111111111111111111111111111111112222"
#     text = text.encode('utf-8')
#     text = conv(text, 32)
#     print(text)
#     i = 0
#     getData = ""
#     for j in text:
#         X = a.runMaster(i, X)
#         # print(len(j))
#         sendData = aes.encrypt_ECB_by(j, X[0])
#         temp = aes.decrypt_ECB(sendData, X[0])
#         print(temp)
#         print(sendData.hex())
#         getData += temp
#         i += 1
#     print(getData)
# """
# """
# for i in range(100):
#         UK = a.createUk(X, Y)
#         Um = a.createUm(X)
#         X = a.runMaster(i, X)
#         sendData = aes.encrypt_ECB(impData, X[0])
#         # print(int(impData.encode('utf-8')))
#         Us = b.createUs(Y)
#         Y = b.runSlave(i, Y, Um)
#         getData = aes.decrypt_ECB(bytes.fromhex(sendData.hex()), Y[0])
#         # show data
#         if (show_data(X, Y, Um, Us, UK, sendData, getData, j)):
#             print("----------------------------------------------")
#             print("同步所需次數", i + 1)
#             if (MaxTimes <= i):
#                 MaxTimes = i
#             times += (i + 1)
#             break
#             """

# def chunks(l, n):
#     temp = list(l[i:i + n] for i in range(0, len(l), n))
#     return temp

# from PIL import Image
# from PIL import ImageDraw
# import numpy as np
# array = aes.picture_to_RGB(Image.open('lena.png'))
# tt = []
# (W, H) = (512, 512)
# for x in range(W):
#     for y in range(H):
#         for c in range(3):
#             tt.append(array[x][y][c])

# array = tt

# i = 0
# t = 0
# tt = 0
# ss = []
# oo = []
# soso = 0
# for i in range(0, W * H * 3 + 1, 16):
#     if i != 0:
#         tt += 1
#         if tt > 33:
#             break
#         temp = ""
#         for y in range(t, i):
#             if array[y] < 16:
#                 temp += "0" + hex(array[y])[2:]
#             else:
#                 temp += hex(array[y])[2:]
#         # print("圖片原始：", bytes.fromhex(temp).hex(), array[t:i])
#         #  bytes.fromhex(temp),
#         print(bytes.fromhex(temp).hex())
#         sendData = aes.encrypt_ECB_by(bytes.fromhex(temp), X[0])
#         temp = aes.decrypt_ECB_by(sendData, X[0])
#         soso += 1
#         sendData_N = []
#         temp_N = []
#         for s in sendData:
#             sendData_N.append(s)
#             ss.append(s)
#         for s in temp:
#             temp_N.append(s)
#             oo.append(s)
#         print("圖片加密：", sendData.hex(), sendData_N)
#         # print("圖片解密: ", temp.hex(), temp_N)
#         # print("---------------------------------------")
#     t = i

# ss = chunks(ss, 3)
# ss = chunks(ss, 512)
# oo = chunks(oo, 3)
# oo = chunks(oo, 512)
# print(len(ss))
# # print(ss)
# array = np.array(ss)
# im = Image.fromarray(array.astype('uint8'))
# im.save("im.png")
# print(ss[0][0], ss[1][0])
# array = np.array(oo)
# im = Image.fromarray(array.astype('uint8'))
# im.save("img.png")
# print(soso)