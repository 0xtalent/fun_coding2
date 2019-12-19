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
            # category_names[index]
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + category_link, callback=self.parse_maincategory, meta={'maincategory_name':category_names[index]})

    def parse_maincategory(self, response):
        print("parse_maincategory", response.meta['maincategory_name'])

        best_items = response.css('div.best-list')
        for index, item in enumerate(best_items[1].css('li')):
            title = item.css('a.itemname::text').get()
            ori_price = item.css('div.o-price::text').get()
            dis_price = item.css('div.s-price strong span span::text').get()
            discount_percent = item.css('div.s-price em::text').get()
        print(title, ori_price, dis_price, discount_percent)