# import自動修復 程式碼片段Stste
lestModName = ""
while 1:
    try:
        import sys
        import os
        sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
        # 要import的東西放這下面
        import csv
        import time
        import googlesheet
        import numpy as np
        import sys
        import pandas as pd
    except (ModuleNotFoundError, ImportError):  # python import error
        err = str(sys.exc_info()[1])[17:-1]
        if (lestModName != err):
            print("缺少mod: " + err + " 正在嘗試進行安裝")
            os.system("pip install " + err)
            lestModName = err
        else:
            print("無法修復import問題 請人工檢查", "mod name: " + err)
            sys.exit()
        del err
    else:
        del lestModName
        break
# import自動修復 程式碼片段

url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"


def webget():
    sheet = googlesheet.GoogleSheet()
    sheet.init("database")
    res = pd.read_html(url)
    currency = res[0].ix[:, 0:5]
    # currency.colums=[u'幣別',u'現金匯率_本行買入',u'現金匯率_本行賣出',u'即期匯率_本行買入',u'即期匯率_本行賣出']
    # currency.colums=[1,2,3,4,5]
    colums = [u'幣別', u'現金匯率_本行買入', u'現金匯率_本行賣出', u'即期匯率_本行買入', u'即期匯率_本行賣出']
    ans = []
    for i in range(len(currency)):
        if 1:
            ans.append([])
            for j in range(len(currency.ix[i])):
                if j == 0:
                    currency.ix[i][0] = currency.ix[i][0][currency.ix[i][0].find("(") + 1:currency.ix[i][0].find("(") + 4]
                    ans[i].append(currency.ix[i][j])
                else:
                    if (currency.ix[i][j] == '-'):
                        pass
                    else:
                        ans[i].append(currency.ix[i][j])
    df = pd.DataFrame(data=[ans[0], ans[18]], columns=colums)

    print(df["即期匯率_本行賣出"][0])

    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(sheet.insert_row([str(localtime), df["即期匯率_本行賣出"][0], df["即期匯率_本行賣出"][0]], 2))

    with open(sys.path[0] + "/test.csv", "a", encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        
        # 寫入writerows
        writer.writerows([[localtime, df["即期匯率_本行賣出"][0], df["即期匯率_本行賣出"][1]]])


# 開啟輸出的 CSV 檔案

# print(currency.ix[i][0][currency.ix[i][0].find("(")+1:currency.ix[i][0].find("(")+4])

# currency.ix[i][0][currency.ix[i][0].find("(")+1:currency.ix[i][0].find("(")+3]
webget()
