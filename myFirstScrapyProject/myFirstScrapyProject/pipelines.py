# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class DeleteNullTitlePipeline(object):

    def process_item(self, item, spider):
        title = item['title']
        if title != "(None,)":
            raise ("hi")
            return item
        else:
            raise DropItem('found null title %s', item)


class MyfirstscrapyprojectPipeline(object):

    def process_item(self, item, spider):
        type(item)
        if type(item['push']) == 'str':
            item['push'] = int(item['push'])
        return item
