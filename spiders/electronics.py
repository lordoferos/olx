# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor




class ElectronicsSpider(CrawlSpider):
    name = 'electronics'
    allowed_domains = ['www.olx.com']
    start_urls = [
        'https://www.olx.com/computers-accessories/',
        'https://www.olx.com/tv-video-audio/',
        'https://www.olx.com/games-entertainment/'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
        callback="parse_item",
        follow=True),)

    def parse_item(self, response, parse_detail_page):
        item_links = response.css('.gallerywide > .cus_ad_item > .detailsLinkPromoted::attr(href)').extract()
        
        print('Processing..' + response.url)
        
