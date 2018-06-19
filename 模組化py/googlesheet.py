# import自動修復 程式碼片段Stste
err = ""
lestModName = ""
while 1:
    try:
        import sys
        import os
        # 要import的東西放這下面
        import gspread  # 雲端
        from oauth2client.service_account import \
            ServiceAccountCredentials  # google oauth
    except ModuleNotFoundError:
        err = str(sys.exc_info()[1])[17:-1]
        if (lestModName != err):
            print("缺少mod: " + err + " 正在嘗試進行安裝")
            os.system("pip install " + err)
            lestModName = err
        else:
            print("無法修復import問題 請人工檢查", "mod name: " + err)
            sys.exit()
    else:
        del lestModName, err
        break
# import自動修復 程式碼片段


class GoogleSheet():

    def init(self, sheetName):
        try:
            global scope, creds, client, sheet
            scope = ['https://www.googleapis.com/auth/drive']  # host sever
            creds = ServiceAccountCredentials.from_json_keyfile_name(sys.path[0] + '/client_secret.json', scope)  # atuh 驗證 記得準備認證用的檔案
            client = gspread.authorize(creds)  # 雲端硬碟宣告
            sheet = client.open(sheetName).sheet1  # 試算表宣告(括號內要改成你自己雲端裡面的sheet檔案)
            print("找到資料表: " + str(sheet))
        except gspread.exceptions.SpreadsheetNotFound:
            print('沒找到sheet檔案，請確認後再一次')
            sys.exit()
        except FileNotFoundError:
            print('沒找到client_secret.json，請確認後再一次')
            sys.exit()

    def update(self, row, lat, data):
        try:
            sheet.update_cell(row, lat, data)
        except:
            return "update error"
        else:
            return "ok"

    def cell(self, row, lat):
        try:
            res = sheet.cell(row, lat).value
        except:
            return "cell error"
        else:
            return res

    def row_values(self, line):
        try:
            res = sheet.row_values(line)
        except:
            return "cell error"
        else:
            return res


# init("你要開的sheet檔案名稱")
# ---------------指令簡約表
# sheet.insert_row(data, 3)  # 在row 3 插入資料
# values_list = sheet.row_values(3) # 讀取第3行全部資料
# values_list = sheet.cell(6,11).value # 讀取第6行 11列 的資料
# sheet.update_cell(6,11,data) # 更新第6行 11列 的資料
# T.I.P.S. 回傳回來的東西是 STR 或 STR的list[]
