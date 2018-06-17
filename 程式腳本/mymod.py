# -*- coding: utf-8 -*-
# 少女前線 使用腳本
#import cv2

import time
import win32api
import win32gui
import win32con
import pyautogui


def Findwindows(X):
    dlg = win32gui.FindWindow(None, X)  # 依照視窗標題尋找句柄
    # print (dlg)
    if dlg != 0:
        win32gui.ShowWindow(dlg, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(dlg)  # 將視窗至回前景
        time.sleep(2)
        arry = win32gui.GetWindowRect(dlg)  # 獲得視窗座標(起始點X,起始點Y,終點X,終點Y)
        print(u"成功找到視窗，視窗句炳為:", dlg)
        # print (u"視窗位置:",arry[0],arry[1])
        # print (u"視窗大小",arry[2]-arry[0],arry[3]-arry[1])
        return dlg, arry
    else:
        # print (u"視窗尋找失敗請確定視窗存在")
        return -1


def Findimg(humd, file):  # 視窗前景找圖
    win32gui.ShowWindow(humd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(humd)  # 將視窗至回前景
    x = pyautogui.locateOnScreen(file)
    print(u"這是debug X值:", x)
    if (x is not None):
        imglocation = x[0] + x[2] / 2, x[1] + x[3] / 2
        print(u"抓圖成功")
        return imglocation  # 回傳圖片中央位置
    else:
        print(u"未找到圖片位置")
        return x


# x=Findwindows(u"小算盤")
# huwd,array=x[0],x[1]
# print (x[0])
# pyautogui.moveTo(Findimg(x[0],'D:\\程式\\python\\re.png'))
