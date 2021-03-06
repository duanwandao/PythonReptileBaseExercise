# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from selenium import webdriver

class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['guazi.com']
    # start_urls = ['https://www.guazi.com/bj/buy/']
    def start_requests(self):
        yield SplashRequest("https://www.guazi.com/bj/buy/", callback=self.parse, args={'wait': 1})

    def parse(self, response):
        print(response.text)
