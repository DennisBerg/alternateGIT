# -*- coding: utf-8 -*-
import scrapy

from alternate.items import AlternateCases

class alternatecases(scrapy.Spider):
    name = "alternatecases"
    allowed_domains = ["alternate.nl"]
    start_urls = [
    	# behuizingen
        "http://www.alternate.nl/html/highlights/page.html?hgid=205&tgid=944&tk=7&lk=9276",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="highlightMatrix"]'):
            item = AlternateCases()
            item['title'] = sel.xpath('a/span[@class="name"]/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['price'] = sel.xpath('a/span[@class="price"]/text()').extract()
            yield item


