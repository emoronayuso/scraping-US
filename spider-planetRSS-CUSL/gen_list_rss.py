from scrapy import Spider, Item, Field
from scrapy.selector import Selector
import re

class ItemRss(Item):
    link = Field()

class CUSLSpider(Spider):
    name = 'planet_spider'
    start_urls =  ['http://www.concursosoftwarelibre.org/1415/proyectos']

    def parse(self, response):
        item = ItemRss()
        sel = Selector(response)
        
        for link in sel.xpath('//div/a').re(r'.+RSS</a>'):
            item["link"] = link
            yield item
