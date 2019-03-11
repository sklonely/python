# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
from ..items import MyfirstscrapyprojectItem


class PttSpider(scrapy.Spider):
    count_page = 1
    name = 'ptt'
    allowed_domains = ['www.ptt.cc/']
    start_urls = ['https://www.ptt.cc/bbs/movie/index.html']

    def parse(self, response):
        item = MyfirstscrapyprojectItem()
        for q in response.css('div.r-ent'):

            item['push'] = q.css('div.nrec > span.hl::text').extract_first(),
            item['title'] = q.css('div.title > a::text').extract_first(),
            item['href'] = q.css('div.title > a::attr(href)').extract_first(),
            item['date'] = q.css('div.meta > div.date ::text').extract_first(),
            item['author'] = q.css('div.meta > div.author ::text').extract_first(),

            yield (item)
        # 下頁處理
        next_page_url = response.css('div.action-bar > div.btn-group > a.btn::attr(href)')[3].extract()
        if (next_page_url) and (self.count_page < 10):
            self.count_page = self.count_page + 1
            new = response.urljoin(next_page_url)
        else:
            raise CloseSpider('close it')
        yield scrapy.Request(new, callback=self.parse, dont_filter=True)


class PttSpider(scrapy.Spider):
    count_page = 1
    name = 'Catch_stock_information'
    allowed_domains = ['www.twse.com.tw/']
    start_urls = ['https://www.ptt.cc/bbs/movie/index.html']

    def parse(self, response):
        item = MyfirstscrapyprojectItem()
        for q in response.css('div.r-ent'):

            item['push'] = q.css('div.nrec > span.hl::text').extract_first(),
            item['title'] = q.css('div.title > a::text').extract_first(),
            item['href'] = q.css('div.title > a::attr(href)').extract_first(),
            item['date'] = q.css('div.meta > div.date ::text').extract_first(),
            item['author'] = q.css('div.meta > div.author ::text').extract_first(),

            yield (item)
        # 下頁處理
        next_page_url = response.css('div.action-bar > div.btn-group > a.btn::attr(href)')[3].extract()
        if (next_page_url) and (self.count_page < 10):
            self.count_page = self.count_page + 1
            new = response.urljoin(next_page_url)
        else:
            raise CloseSpider('close it')
        yield scrapy.Request(new, callback=self.parse, dont_filter=True)
