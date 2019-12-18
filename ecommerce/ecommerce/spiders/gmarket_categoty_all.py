# -*- coding: utf-8 -*-
import scrapy


class GmarketCategotyAllSpider(scrapy.Spider):
    name = 'gmarket_categoty_all'

    def start_requests(self):
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers', callback=self.parse)

    def parse(self, response):
        pass
