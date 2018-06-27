# import自動修復 程式碼片段Stste
lestModName = ""
while 1:
    try:
        import sys
        import os
        sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
        # 要import的東西放這下面
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.action_chains import ActionChains
        import time
    except (ModuleNotFoundError, ImportError):  # python import error
        err = str(sys.exc_info()[1])[17:-1]
        if (lestModName != err):
            print("缺少mod: " + err + " 正在嘗試進行安裝")
            os.system("pip install " + err)
            lestModName = err
        else:
            print("無法修復import問題 請人工檢查", "mod name: " + err)
            sys.exit()
    else:
        del lestModName
        break
# import自動修復 程式碼片段

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
iedriver = "C:\IEDriverServer.exe"
driver = webdriver.Ie(iedriver)
driver.get("http://cu.stu.edu.tw/")
actions = ActionChains(driver)
# 顯示標題
print(driver.title)
time.sleep(0.8)
# 找到搜尋框
uesElement = driver.find_element_by_name("username")
paswElement = driver.find_element_by_name("password")
loginElement = driver.find_element_by_class_name("cssLoginBtn")
print(driver.find_element_by_name("username").location)
# 搜尋框輸入字
uesElement.send_keys("s16115106" + Keys.TAB + Keys.ENTER)
# paswElement.send_keys(Keys.ENTER)
# 提交
time.sleep(3.8)
