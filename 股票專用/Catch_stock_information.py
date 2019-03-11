import datetime
import time
from io import StringIO
import sys
import numpy as np
import pandas as pd
import requests
import aiohttp
import asyncio

url = 'http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date='


# URL='https://morvanzhou.github.io/'
async def job(session, date):
    URL = url + str(date).split(' ')[0].replace('-', '') + '&type=ALL'
    r = await session.post(URL)  # 等待并切换
    return r


async def main(loop):
    date = '2019-02-26'
    async with aiohttp.ClientSession() as session:  # 官网推荐建立 Session 的形式
        tasks = [loop.create_task(job(session, date)) for _ in range(1)]
        finished, unfinished = await asyncio.wait(tasks)  # 获取所有结果
        print(finished.result)


t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print("Async total time:", time.time() - t1)

# async def get_url_job(session, date):
#     URL = url + str(date).split(' ')[0].replace('-', '') + '&type=ALL'
#     response = await session.post(URL)  # 等待并切换
#     return str(response.url)

# async def main(loop):
#     async with aiohttp.ClientSession() as session:  # 官网推荐建立 Session 的形式
#         tasks = loop.create_task(get_url_job(session, '2019-02-26'))
#         finished, unfinished = await asyncio.wait(tasks)
#         print(finished)

# def crawl_price(date):
#     r = requests.post(url + str(date).split(' ')[0].replace('-', '') + '&type=ALL')
#     ret = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) for i in r.text.split('\n') if len(i.split('",')) == 17 and i[0] != '='])), header=0)
#     ret = ret.set_index('證券代號')
#     ret['成交金額'] = ret['成交金額'].str.replace(',', '')
#     ret['成交股數'] = ret['成交股數'].str.replace(',', '')
#     return ret

# def all_crawl_price(days):
#     data = {}
#     n_days = days
#     date = datetime.datetime.now()
#     fail_count = 0
#     allow_continuous_fail_count = 5
#     while len(data) < n_days:
#         print('parsing', date)
#         # 使用 crawPrice 爬資料
#         try:
#             # 抓資料
#             data[date] = crawl_price(date)
#             print('success!')
#             fail_count = 0
#         except:
#             # 假日爬不到
#             print('fail! check the date is holiday')
#             fail_count += 1
#             if fail_count == allow_continuous_fail_count:
#                 raise ('have some error')
#                 break

#         # 減一天
#         date -= datetime.timedelta(days=1)
#         time.sleep(10)

#     return data

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main(loop))
# daaa.to_csv('out.csv')
# date = datetime.datetime.now()
# date -= datetime.timedelta(days=6)
# data = crawl_price(date)
# data.to_csv('db/Result.csv')
# df = pd.read_csv("db/Result.csv")
# df1 = pd.DataFrame(df["證券代號"] + "-" + df["證券名稱"])

# for i in df.columns:
#     if i != "收盤價":
#         df = df.drop(columns=[i])
# df = pd.concat([df1, df], axis=1)
# df = df.rename(columns={0: "證券代號-證券名稱"})
# print(df)
#print(data["收盤價"]) df["證券名稱"]
# print(data)