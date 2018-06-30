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
        import http.cookiejar
        import requests
        import time
        from lxml import html
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
# 使用者帳密
username = ''
password = ''
##
forum_url = "http://www02.eyny.com/"  # 論壇網址
novel_sort_name = []  # 小說分類 [["玄幻魔法小說", html], ..]
novel_sort_maxpage = 0  # 小說
novel = []
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://www.eyny.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
auth_cookies = ''

##


# 登入論壇
def get_auth():
    session_requests = requests.session()  # 建立requests連接
    session_requests.headers = headers  # 初始化headers

    # 取得from_hahs 跟 login_hahs
    result = session_requests.get(forum_url + "member.php?mod=logging&action=login")
    tree = html.fromstring(result.text)
    time.sleep(0.1)
    from_hahs = list(set(tree.xpath('//*[@id="scbar_form"]/input[2]/@value')))[0]
    login_hahs = list(set(tree.xpath('//*[@name="login"]/@action')))[0]
    ##

    # 創建POST 用的data from
    payload = {'formhash': from_hahs, 'referer': 'http://www.eyny.com/index.php', 'loginfield': 'username', 'username': 'asd1953721', 'password': 'asd195375', 'questionid': '0', 'answer': '', 'cookietime': '2592000'}
    ##

    # 發送POST請求 取得auth cookies
    result = session_requests.post(forum_url + login_hahs, data=payload, headers=headers)
    auth = str(list(result.cookies)[0])
    print("獲取登入認證碼: ", auth[auth.find(" "):auth.find("=")], auth[auth.find("=") + 1:auth.find(" f")])
    ##

    # 獲取登入狀態
    auth = [auth[auth.find(" "):auth.find("=")], auth[auth.find("=") + 1:auth.find(" f")]]
    result = session_requests.get(forum_url + 'index.php', cookies=result.cookies)
    soup = BeautifulSoup(result.text, "html.parser")
    tag = soup.find_all('strong')
    if (tag[0].text == "登錄"):
        print("登入失敗")
        sys.exit()
    else:
        print("歡迎登入 :", tag[0].text)

    ##

    return result.cookies


def novel_all_page_Download(novel_name, novel_url_main, novel_max_page, res_cookies):
    # session init
    session_requests = requests.session()  # 建立requests連接
    session_requests.headers = headers  # 初始化headers
    # page變數管制
    novel_url_main = novel_url_main.split("-1-")
    page = 1
    ##
    print("小說: ", novel_name, "下載中...")

    result = session_requests.get(forum_url + 'thread-11728982-1-BX4TQDHP.html', cookies=res_cookies)

    soup = BeautifulSoup(result.text, "html.parser")
    a_tags = soup.find_all('td', {"class": "t_f"})
    print(a_tags[1].text)
    for tags in a_tags:
        with open('G:\我的云端硬盘\小說用\file.txt', 'a') as f:
            page = str(tags.text)
            page = page.replace(u'\xa0', u' ')
            f.write(page)


def novel_page_get():

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
                # print(a_taglist[0])
                novel.append([a_taglist[0].string, a_taglist[1].string, a_taglist[1].get('href')])
    # 獲取最大maxpage
    a_tags = soup.find_all('a', {"class": "last"})[0].text[4:]
    print(a_tags)
    ##
    for i in range(len(novel)):
        print(novel[i])
        # if (str(type(tag.a)) != "<class 'NoneType'>"):
        # print(tag.a.string)

    html = urllib.request.urlopen(forum_url + novel[0][2])
    soup = BeautifulSoup(html, "html.parser")


novel_page_get()