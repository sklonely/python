# -- coding: utf-8 --
import requests
import threading as thd
import pandas as pd # 引用套件並縮寫為 pd
import time
import csv
exitflag=1#RateWebGet忙綠旗標
fileflag=1#檔案旗標
def main():
    RateWebGet()

def  RateWebGet():
	while 1:
		try:
			exitflag=0# 旗標忙碌中
			fileflag=0
			print("RateWebGet start")
			r = requests.get('https://tw.rter.info/capi.php')
			currency = r.json()

			rate = currency['USDTWD']['Exrate']
			ftime = currency['USDTWD']['UTC']
			print("USD -> TWD rate: ", rate, " Time: ", ftime)
			f = open("rate.txt", "a+")
			f.write("USD -> TWD rate: ")
			f.write(str(rate))
			f.write(" Time: ")
			f.write(str(ftime))
			f.write("\n")
			f.close()
			fileflag=1
			print("RateWebGet end")
			time.sleep(180)
			exitflag=1#歸還旗標
		except:
			break

def RateFileGet():
    if(fileflag==1):#判斷旗標忙碌?
        Vreturn=[]
        f=open("rate.txt", "r")
        strfl=f.readlines()
        i=0
        for strf in strfl:
            Vreturn.append([])
            Vreturn[i].append(float(strf[strf.find("rate: ")+6:strf.find("Time: ")-1]))#將Rate存在[ "Rate", "時間" ]
            Vreturn[i].append(strf[strf.find("Time: ")+6:strf.find("Time: ")+25])#將時間存在[ "Rate", "時間" ]

            i=i+1
        f.close()
        #print(Vreturn)#除錯用
        return Vreturn
    else:#若旗標忙碌 等1秒 再呼叫自己
        time.sleep(1)
        RateFileGet()

def RateCsvGet():
    f=csv.DictReader("rate")

    f.close()


#if __name__ == '__main__':
    #while 1:
        #if(exitflag==1):
            #t=thd.Thread(target=RateWebGet())
main()