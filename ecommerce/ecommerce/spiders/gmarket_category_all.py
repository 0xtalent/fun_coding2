# -*- coding: utf-8 -*-
import scrapy


class GmarketCategoryAllSpider(scrapy.Spider):
    name = 'gmarket_category_all'

    def start_requests(self):
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers', callback=self.parse)

    def parse(self, response):
        category_links = response.css('div.gbest-cate ul.by-group li a::attr(href)').getall()
        category_names = response.css('div.gbest-cate ul.by-group li a::text').getall()
        for index, category_link in enumerate(category_links):
            print('http://corners.gmarket.co.kr' + category_link, category_names[index])