# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class EcommercePipeline(object):
    def process_item(self, item, spider):
        print('process_item', item)
        if int(item['price'])>10000:
            return item
        else:
            raise DropItem("dropitem",item)