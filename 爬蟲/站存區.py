for i in range(len(list(result.cookies))):
        print(list(result.cookies)[i])
    tree = html.fromstring(result.text)
    # time.sleep(1)
    from_hahs = list(set(tree.xpath('//*[@id="scbar_form"]/input[2]/@value')))[0]
    login_hahs = list(set(tree.xpath('//*[@name="login"]/@action')))[0]
    print(from_hahs, login_hahs)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '162',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'username=asd1953721',
        'Host': 'www.eyny.com',
        'Origin': 'http://www.eyny.com',
        'Referer': 'http://www.eyny.com/member.php?mod=logging&action=login',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }
    payload = {'formhash': from_hahs, 'referer': 'http://www.eyny.com/index.php', 'loginfield': 'username', 'username': 'asd1953721', 'password': 'asd195375', 'questionid': '0', 'answer': '', 'cookietime': '2592000'}

    result = session_requests.post(forum_url + login_hahs, data=payload, headers=headers)
    auth = str(list(result.cookies)[0])
    auth = auth[auth.find(" ") + 1:auth.find(" f") - 1]
    for i in range(len(list(result.cookies))):
        print(list(result.cookies)[i])
    return auth






auth =[]
    authlist = list(result.cookies)
    for i in range(len(list(authlist))):
        x = str(authlist[i])
        #print(authlist[i])
        auth.append(x[x.find(" ") + 1:x.find(" f")])
    print(auth)