from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
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
uesElement.send_keys("s16115106")
time.sleep(0.8)
paswElement.send_keys("lonely1953721" + Keys.ENTER)
# paswElement.send_keys(Keys.ENTER)
# 提交
time.sleep(3.8)