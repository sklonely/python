import requests
from bs4 import BeautifulSoup
import matplotlib # 繪圖
import matplotlib.pyplot as plt  # 繪圖

url = 'https://www.cpc.com.tw/'
html = requests.get(url)
html.encoding = "utf-8"
sp = BeautifulSoup(html.text, 'html.parser')

data = sp.find_all('b', {'class': 'price'})
print("92無鉛 %s" % data[0].text)
print("95無鉛 %s" % data[1].text)
print("98無鉛 %s" % data[2].text)

# 繪圖區域
price = [float(data[i].text) for i in range(3)]

matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

plt.barh(range(3), price, height=0.7, color='steelblue', alpha=0.8)
plt.yticks(range(3),['92無鉛','95無鉛','98無鉛'])
plt.xlim(25,40)
plt.xlabel('價格 單位 公升/元')
plt.title('中油公司油價圖表')
for x, y in enumerate(price):
    plt.text(y + 0.2, x - 0.1, '%s' % y)
plt.show()

# 結束繪圖

htmllist = html.text.splitlines()
# print(sp.get_text())
# n=0
# for row in htmllist:
#     if "石油" in row:
#         n+=1
#         print(type(row))
# print("找到 {} 次 !".format(n))