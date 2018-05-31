# coding=utf-8
# 导入pymysql的包
import sheet
import pymysql
import pymysql.cursors
import sys
import openpyxl

# 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
# port 必须是数字不能为字符串
db = pymysql.connect(
    host='localhost',
    db='test',
)
print("資料庫連接成功")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
tabNames = sheet.sheetNames()
tabLen = len(tabNames)
# print(tabNames,"_",tabLen,"_",tabCol,"_",tabColLen,"_",tabRow,"_",tabRowLen)
for tab in tabNames:  # 每一個工作表 都當一個tabel
    # ---初始化---
    tabCol = sheet.sheetGetTable(tab)  # 獲取當前工作表的 tabName
    tabColLen = len(tabCol)
    tabRow = sheet.sheetGetData(tab)  # 獲取當前工作表的 tabData
    tabRowLen = len(tabRow)
    # ------------

    # 如果table存在則刪除他
    sql = "DROP TABLE IF EXISTS " + tab
    cursor.execute(sql)

    # 創建table開始
    sql = "CREATE TABLE " + tab + "("
    for i in tabCol:  # 創建指令生成
        if i != tabCol[len(tabCol) - 1]:
            sql = sql + i + " char(50),"
        else:
            sql = sql + i + " char(50));"
    # ---------------- 創建指令生成結束
    print(sql)  # 印出創建指令 供除錯
    cursor.execute(sql)
    # 創建結束

    # 對table輸入資料開始
    sql = "INSERT INTO " + tab + "("  # 通用指令生成
    for i in tabCol:
        if i != tabCol[len(tabCol) - 1]:
            sql = sql + i + ", "
        else:
            sql = sql + i + ") VALUES("
    # ---------------------------- 通用指令生成結束

    sqlt = sql  # 通用指令暫存

    if (tabRowLen == 1):  # 資料只有1筆
        for i in tabRow:  # values指令生成(單筆的)
            if i != tabRow[len(tabRow) - 1]:
                sql = sql + str(i) + ", "
            else:
                sql = sql + str(i) + ");"
    # -------------------- values指令生成結束(單筆的)

    else:  # --------------- 資料多筆
        for row in tabRow:
            temp = sqlt
            for i in row:  # values指令生成(多筆的)
                if i != row[len(row) - 1]:
                    temp = temp + "\'" + str(i) + "\', "
                else:
                    temp = temp + "\'" + str(i) + "\');"
                    sql = temp
                    # ---------------------- values指令生成(多筆的)
                    print(sql)  # 印出資料輸入指令 供除錯
                    cursor.execute(sql)
                    db.commit()
    # 對table輸入資料結束
    # 印出資料表內容 供除錯
    sql = "SELECT * FROM " + tab + ";"
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    # 程式結束

db.close()
print("資料庫關閉_程式結束")
# cursor.execute("DROP TABLE IF EXISTS TEST")
"""
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS TEST")
# 创建表指令
sql = ""CREATE TABLE  TEST(ID char(10),Name char(10));""
# 使用 execute()创建表
cursor.execute(sql)
# 插入指令
sql = ""INSERT INTO TEST(ID, Name) VALUES('A001','Mac');""
sys.stdout.write("\r資料輸入...")
try:
   # 执行sql语句
    cursor.execute(sql)
   # 提交到数据库执行
    db.commit()
except:
   # 如果发生错误则回滚
    print ("error: 資料輸入測試意外")
    db.rollback()

# SQL 查询语句
sql = "SELECT * FROM TEST;"
sys.stdout.write("\r查詢...")
try:
   # 执行SQL语句
    cursor.execute(sql)
   # 获取所有记录列表
    results = cursor.fetchall()
   # 打印结果
    sys.stdout.write("\r 資料內容: ")
    print (results)
except:
    print ("Error: 讀取發生錯誤")

# 关闭数据库连接
db.close()
print ("資料庫關閉_程式結束")
"""
