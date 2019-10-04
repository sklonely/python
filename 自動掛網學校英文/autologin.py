# import自動修復 程式碼片段Stste
lestModName = ""
err = ""
while 1:
    try:
        import sys
        import os
        # 要import的東西放這下面
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.action_chains import ActionChains
        import time
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

iedriver = "D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(iedriver)
driver.get("http://cu.stu.edu.tw/learn/index.php")
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
uesElement.send_keys("*" + Keys.TAB)
paswElement.send_keys("*" + Keys.ENTER)
# 提交
time.sleep(2.8)
classElement = driver.find_element_by_xpath("//*[@id='tabsCourse']/tbody/tr[6]/td[1]/div/a")
print(classElement)
