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
username = 'asd1953721'
password = 'asd195375'
##
forum_url = "http://www02.eyny.com/"  # 論壇網址
novel_sort = []  # 小說分類 [["玄幻魔法小說", html], ..]
novel_sort_maxpage = 0  # 小說
novel = []  # 小說分類 ["小說分類","小說名稱","小說網址"]

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
    payload = {'formhash': from_hahs, 'referer': 'http://www.eyny.com/index.php', 'loginfield': 'username', 'username': username, 'password': password, 'questionid': '0', 'answer': '', 'cookietime': '2592000'}
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

    return session_requests


def novel_all_page_Download(novel, session_requests):
    # session init
    result = session_requests.get(forum_url + novel[2])
    soup = BeautifulSoup(result.text, "html.parser")
    if soup.find_all('a', {"class": "last"}):
        maxpage = soup.find_all('a', {"class": "last"})[0].text[4:]
        url = novel[2].split('-1-')
        print(url)
    else:
        url = novel[2]
        maxpage = 1

    maxpage = 10  # debug
    time.sleep(0.2)
    # 開始下載小說
    for i in range(int(maxpage)):
        pages = i + 1
        novel_sort_page_url = url[0] + '-' + str(pages) + '-' + url[1]  # 合成網址
        result = session_requests.get(forum_url + novel_sort_page_url)
        # 當前頁面本文下載到txt
        soup = BeautifulSoup(result.text, "html.parser")
        a_tags = soup.find_all('td', {"class": "t_f"})
        # 將本文存入檔案
        for tags in a_tags:
            with open('G:\我的云端硬盘\小說用\玄幻魔法小說\\' + novel[1] + '.txt', 'a', encoding='UTF-8') as f:
                page = str(tags.text)
                f.write(page)
        print("正在下載:", novel[1], pages, "/", str(maxpage), "頁")
        time.sleep(0.2)


def novel_sort_page_get():

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
                novel_sort.append([tag.string, tag.a.get('href')])
    for a in novel_sort:
        print(a)


def novel_sort_data_get(novel_sort):
    # 頁數網址處理
    html = urllib.request.urlopen(forum_url + novel_sort[1])
    soup = BeautifulSoup(html, "html.parser")
    maxpage = soup.find_all('a', {"class": "last"})[0].text[4:]  # 最大頁數獲得
    # maxpage = 1
    # 第一次近來小說網頁
    title_tag = soup.title
    print("你正在: " + title_tag.string + " 頁面  1/" + str(maxpage))
    # 取得小說版塊所有小說名稱及網址
    a_tags = soup.find_all('th')  # 獲取當前頁面所有帖子
    for taglist in a_tags:  # 將公告去除
        a_taglist = taglist.find_all('a', limit=2)
        # 取得當前頁面上所有小說的 分類 名稱 連載狀況
        if taglist.get("class") is not None:
            if taglist.get("class")[0] == "new":
                novel.append([a_taglist[0].string, a_taglist[1].string, a_taglist[1].get('href')])  # 儲存格式[類別, 名稱, 網址]
    a_tags = soup.find_all('div')
    for taglist in a_tags:
        if taglist.get("class") is not None:
            if taglist.get("class")[0] == "pg":
                novel_sort[1] = taglist.find_all('a')[-1].get("href")
                break
    # 第二次以上
    for i in range(1, int(maxpage)):
        page = i + 1
        # 小說版塊頁面下載
        # print(novel_sort_page_url)
        html = urllib.request.urlopen(forum_url + novel_sort[1])
        soup = BeautifulSoup(html, "html.parser")
        title_tag = soup.title
        print("正在收集小說資料... 頁面: " + title_tag.string + " 頁面 " + str(page) + "/" + maxpage)
        # 取得小說版塊所有小說名稱及網址
        a_tags = soup.find_all('th')  # 獲取當前頁面所有帖子
        for taglist in a_tags:  # 將公告去除
            a_taglist = taglist.find_all('a', limit=2)
            # 取得當前頁面上所有小說的 分類 名稱 連載狀況
            if taglist.get("class") is not None:
                # print(a_taglist)
                if a_taglist[0].string != "公告":
                    novel.append([a_taglist[0].string, a_taglist[1].string, a_taglist[1].get('href')])  # 儲存格式[類別, 名稱, 網址]
        a_tags = soup.find_all('div')
        for taglist in a_tags:
            if taglist.get("class") is not None:
                if taglist.get("class")[0] == "pg":
                    novel_sort[1] = taglist.find_all('a')[-1].get("href")
                    break
        time.sleep(0.3)

    # 將結果存入txt檔中 檔案名稱[(小說類別)目錄.txt] 內容格式: [分類][小說][網址]
    try:
        with open('G:/我的雲端硬碟/小說用/' + novel_sort[0] + '目錄.txt', 'w+', encoding='UTF-8') as f:
            f.write(novel_sort[0] + "所有小說目錄:\n=========================================================================\n")
            for i in range(len(novel)):  # 將小說名稱 網址 打印出來
                f.write(novel[i][0] + ",")
                f.write(novel[i][1] + ",")
                f.write(novel[i][2] + "\n")
                print(novel[i])
    except FileNotFoundError:
        with open('G:/我的云端硬盘/小說用/' + novel_sort[0] + '目錄.txt', 'w+', encoding='UTF-8') as f:
            f.write(novel_sort[0] + "所有小說目錄:\n=========================================================================\n")
            for i in range(len(novel)):  # 將小說名稱 網址 打印出來
                f.write(novel[i][0] + ",")
                f.write(novel[i][1] + ",")
                f.write(novel[i][2] + "\n")
                print(novel[i])


# get_auth()
def one_novel_download(novelnaem):
    novel = search_local("放開那個女巫")
    get_auth()
    novel_all_page_Download(novel[0], get_auth())


def run_sort():
    novel_sort_page_get()
    for i in novel_sort:
        novel_sort_data_get(i)
        time.sleep(10)


def search_local(novelnaem):
    ls = ["玄幻魔法小說目錄.txt", "武俠修真小說目錄.txt", "科幻偵探小說目錄.txt", "原創言情小說目錄.txt", "都市小說目錄.txt", "輕小說目錄.txt", "其他小說目錄.txt"]
    flag = False
    novel_re = []
    for i in ls:
        print("尋找中... 檔案:" + i)
        with open('G:/我的云端硬盘/小說用/' + i, 'r', encoding='UTF-8') as f:
            novel_list = f.readlines()
            novel_list = novel_list[2:]
        novel = []
        for s in novel_list:
            s = s[:-1]
            novel.append(s.split(","))
        for s in novel:
            if s[1].find(novelnaem) > 0:
                print("在 '" + i + "' 找到了:\n", s)
                novel_re.append(s)
                print(novel_re)
                flag = True
                break
        if flag:
            return novel_re


novel_sort_page_get()