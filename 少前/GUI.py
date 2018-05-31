import tkinter as tk
import mymod as my
import random
import time
import win32api
import win32gui
import win32con
from ctypes import *
# 宣告區
window = tk.Tk()
window.title("少女前線腳本")
window.geometry('800x800')
G_filg_INT = 0

# 基礎變數定義


def StateTranslation(X):  # 變數意義轉換
    level = X
    if level == -1:
        return str("檢查中")
    elif level == 0:
        return str("空閒中")
    elif level == 1:
        return str("後情中(空閒")
    elif level == 2:
        return str("後情中(忙碌")
    elif level == 3:
        return str("戰役中")
    elif level == 4:
        return str("檢查環境")
    elif level == 5:
        return str("檢查獎勵")
    elif level == 6:
        return str("領獎中")


var = tk.StringVar()
var.set("現在狀態: " + StateTranslation(G_filg_INT))
tk.Label(window, textvariable=var).place(x=350, y=10, anchor='nw')


def cheak():  # 檢查按鈕按下
    G_filg_INT = 1  # 忙碌旗標
    StateTranslation(G_filg_INT)
    print("正在檢查相關元素")
    main()
    G_filg_INT = 0  # 歸還旗標
    StateTranslation(G_filg_INT)
    var.set("現在狀態: " + StateTranslation(G_filg_INT))


tk.Button(window, text="檢查", command=cheak).place(x=380, y=40, anchor='nw')
LAB = tk.Label(window, text="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬").place(x=0, y=70, anchor='nw')
LAB1 = tk.Label(window, text="《 後勤相關 》" + "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬✪✪✪▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬" + "《 戰役相關  》").place(x=20, y=100, anchor='nw')
# 4大空格字典
T2L = {0: tk.Entry(window), 1: tk.Entry(window), 2: tk.Entry(window), 3: tk.Entry(window)}
T2R = {0: tk.Entry(window), 1: tk.Entry(window), 2: tk.Entry(window), 3: tk.Entry(window)}
waveL = {0: tk.Entry(window), 1: tk.Entry(window), 2: tk.Entry(window), 3: tk.Entry(window)}
waveR = {0: tk.Entry(window), 1: tk.Entry(window), 2: tk.Entry(window), 3: tk.Entry(window)}
# 排版迴圈
for i in range(4):
    for j in range(9):
        if j == 0:
            T1 = tk.Label(window, text="梯隊")
            T1.place(x=110, y=150 + i * 30, anchor='nw')
        if j == 1:
            T2L[i] = tk.Entry(window, show=None)
            T2L[i].place(x=140, y=150 + i * 30, anchor='nw', width=20)
        if j == 2:
            T3 = tk.Label(window, text="關卡")
            T3.place(x=170, y=150 + i * 30, anchor='nw')
        if j == 3:
            waveL = tk.Entry(window, show=None)
            waveL.place(x=200, y=150 + i * 30, anchor='nw', width=20)
        if j == 4:
            T3 = tk.Label(window, text="|||")
            T3.place(x=390, y=150 + i * 30, anchor='nw')
        if j == 5:
            T1 = tk.Label(window, text="梯隊")
            T1.place(x=510, y=150 + i * 30, anchor='nw')
        if j == 6:
            T2R = tk.Entry(window, show=None)
            T2R.place(x=540, y=150 + i * 30, anchor='nw', width=20)
        if j == 7:
            T3 = tk.Label(window, text="關卡")
            T3.place(x=570, y=150 + i * 30, anchor='nw')
        if j == 8:
            waveR = tk.Entry(window, show=None)
            waveR.place(x=600, y=150 + i * 30, anchor='nw', width=20)


def ger():  # 測試按鈕
    for i in range(4):
        print(T2L[i].get())


tk.Button(window, text="text", command=ger).place(x=20, y=700)

# 下方win32操作函數


def move_click(x, y):  # 移動後點
    windll.user32.SetCursorPos(x, y)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 10, 10)


def clickLeftCur():  # 模擬點
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 10, 10)


def moveCurPos(x, y):  # 模擬移動
    windll.user32.SetCursorPos(x, y)


def getCurPos():  # 取得游標
    return win32gui.GetCursorPos()


# def FindPic(ux,uy,dx,dy,path,like):#模糊找圖
def move_down(x, y):
    windll.user32.SetCursorPos(x, y, rw, ry)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 10, 10)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, rw, ry)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 10, 10)


def main():
    dlg = my.Findwindows(u"夜神模擬器")  # 依照視窗標題尋找句柄
    if dlg != 0:
        # print (dlg)
        win32gui.ShowWindow(dlg[0], win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(dlg[0])  # 將視窗至回前景
        time.sleep(2)
        arry = win32gui.GetWindowRect(dlg[0])  # 獲得視窗座標(起始點X,起始點Y,終點X,終點Y)
        print(u"視窗位置:", arry[0], arry[1])
        print(u"視窗大小", arry[2] - arry[0], arry[3] - arry[1])

        # 以上獲取視窗資訊
        zeropos = [arry[0], arry[1]]
        moveCurPos(1326, 568)

        my.Findimg(dlg, "img\\OK.png")
        # time.sleep(4)
        # pic = ImageGrab.grab(arry)
        # pic.show()
        #test(zeropos[0], zeropos[1], dlg[0])
    # Fight3_3E(zeropos[0],zeropos[1])

    else:
        print(u"視窗尋找失敗請確定視窗存在")


window.mainloop()
