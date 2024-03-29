# -*- coding: utf-8 -*-
import scrapy
from ecommerce.items import EcommerceItem


class GmarketSpider(scrapy.Spider):
    name = 'gmarket'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        titles = response.css('div.best-list li > a::text').getall()
        prices = response.css('div.best-list ul li div.item_price div.s-price strong span::text').getall()

        for num, title in enumerate(titles):
            doc = EcommerceItem()
            doc['title'] = title
            doc['price'] = prices[num].strip().replace("원", "").replace(",", "")
            yield doc
