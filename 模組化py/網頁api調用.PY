import sys
import os
import requests


url = "https://google.com.tw"
r = requests.get(url)
re = r.json()
print(re)