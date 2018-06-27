# import自動修復 程式碼片段Stste
lestModName = ""
while 1:
    try:
        import sys
        import os
        sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
        # 要import的東西放這下面
        import urllib
        from bs4 import BeautifulSoup
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

# 變數管制
forum_url = "http://www02.eyny.com/"
novel_sort_name = []
novel = []
# 管制區結束

html = urllib.request.urlopen(forum_url + "forum.php?gid=1747")
soup = BeautifulSoup(html, "html.parser")
title_tag = soup.title
print("你正在: " + title_tag.string + "頁面")
# 找個小說版塊位置
a_tags = soup.find_all('h2')

for tag in a_tags:
    for name in ["玄幻魔法小說", "武俠修真小說", "科幻偵探小說", "原創言情小說", "都市小說", "輕小說", "其他小說"]:
        if tag.string == name:
            # print(tag.string, tag.a.get('href'))
            novel_sort_name.append([tag.string, tag.a.get('href')])
print(novel_sort_name[0])

# 小說版塊頁面下載
html = urllib.request.urlopen(forum_url + novel_sort_name[0][1])
soup = BeautifulSoup(html, "html.parser")
title_tag = soup.title
print("你正在: " + title_tag.string + "頁面")
a_tags = soup.find_all('th')  # 獲取當前頁面所有帖子

for taglist in a_tags:  # 將公告去除
    a_taglist = taglist.find_all('a', limit=2)
    # 取得當前頁面上所有小說的 分類 名稱 連載狀況
    if taglist.get("class") is not None:
        if taglist.get("class")[0] == "new":
            temp = []
            # print(a_taglist[0])
            novel.append([a_taglist[0].string, a_taglist[1].string, a_taglist[1].get('href')])


for i in range(len(novel)):
    print(novel[i])
    # if (str(type(tag.a)) != "<class 'NoneType'>"):
    # print(tag.a.string)
