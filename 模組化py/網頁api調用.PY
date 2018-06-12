import sys
import os
import requests


url = "https://info.stu.edu.tw/login/sysLogin.asp"
r = requests.get(url)
url = "https://info.stu.edu.tw/login/SysLoginAction.asp"
r = requests.post(url)
print(r.text)