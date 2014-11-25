# -*- coding: utf-8 -*-
import scrapy

from alternate.items import AlternateHarddisk

class alternateharddisk(scrapy.Spider):
    name = "alternateharddisk"
    allowed_domains = ["alternate.nl"]
    start_urls = [
        # SATA harddisks
	    "http://www.alternate.nl/html/product/listing.html?navId=11584&bgid=8459&tk=7&lk=9563",
        ]
    def parse(self, response):
        for sel in response.xpath('//div[@class="listingResult"]'):
            item = AlternateHarddisk()
            item ['title'] = sel.xpath('').extract()
            yield item



