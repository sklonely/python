# encoding: utf-8
# 少女前線 使用腳本
# import cv2
import random
import time
import win32api
import win32gui
import win32con
import mymod
import GUI
from PIL import ImageGrab
from ctypes import *


def main():
    dlg = mymod.Findwindows(u"夜神模擬器")  # 依照視窗標題尋找句柄
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
        time.sleep(4)
        # pic = ImageGrab.grab(arry)
        # pic.show()
        test(zeropos[0], zeropos[1], dlg[0])
        # Fight3_3E(zeropos[0],zeropos[1])

    else:
        print(u"視窗尋找失敗請確定視窗存在")


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


def test(zx, zy, humd):
    Menu_Repair(zx, zy)
    Menu_Reseaarch(zx, zy)
    Menu_Fight(humd)
    Menu_Dormitory(zx, zy)
    Menu_Factory(zx, zy)
    Menu_Compiled(zx, zy)
    print(u"測試完成")


def Menu_Repair(zx, zy):  #修復
    rx = random.randrange(0, 115)  #誤差
    ry = random.randrange(0, 52)
    windll.user32.SetCursorPos(zx + 630 + rx, zy + 175 + ry)  #修復
    time.sleep(1)


def Menu_Reseaarch(zx, zy):  #研發
    rx = random.randrange(0, 115)  #誤差
    ry = random.randrange(0, 52)
    windll.user32.SetCursorPos(zx + 630 + rx, zy + 275 + ry)  #研發
    time.sleep(1)


def Menu_Fight(humd):  #戰鬥
    rx = random.randrange(0, 115)  #誤差
    ry = random.randrange(0, 52)
    point = mymod.Findimg(humd, "img\\combat.png")
    print(point[0], point[1])
    windll.user32.SetCursorPos(int(point[0] + rx), int(point[1] + ry))  #戰鬥
    time.sleep(1)


def Menu_Dormitory(zx, zy):  #宿舍
    rx = random.randrange(0, 115)  #誤差
    ry = random.randrange(0, 52)
    windll.user32.SetCursorPos(zx + 810 + rx, zy + 175 + ry)  #宿舍
    time.sleep(1)


def Menu_Factory(zx, zy):  #工廠
    rx = random.randrange(0, 115)  #誤差
    ry = random.randrange(0, 52)
    windll.user32.SetCursorPos(zx + 810 + rx, zy + 275 + ry)  #工廠
    time.sleep(1)


def Menu_Compiled(zx, zy):  #編成
    rx = random.randrange(0, 115)  #誤差
    ry = random.randrange(0, 52)
    windll.user32.SetCursorPos(zx + 810 + rx, zy + 375 + ry)  #編成
    time.sleep(1)


def Fight3_3E(zx, zy):
    rx = random.randrange(0, 72)  #誤差
    ry = random.randrange(0, 44)
    Menu_Fight(zx, zy)
    clickLeftCur()
    time.sleep(3)
    move_click(zx + 154 + rx, zy + 352 + ry)  #第三戰役
    time.sleep(1.5)
    move_click(zx + 804 + rx, zy + 156 + ry)  #緊急
    time.sleep(1.5)
    move_click(zx + 512 + rx, zy + 405 + ry)  #關卡3-3
    time.sleep(1.5)
    move_click(zx + 450 + rx, zy + 459 + ry)  #普通作戰
    time.sleep(5)
    rx = random.randrange(0, 25)  #誤差縮小
    ry = random.randrange(0, 25)  #誤差縮小
    move_click(zx + 517 + rx, zy + 339 + ry)  #點選指揮部
    time.sleep(2.5)
    move_click(zx + 853 + rx, zy + 504 + ry)  #部屬
    time.sleep(1)


main()