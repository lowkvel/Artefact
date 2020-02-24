# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Ans1ScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # id
    id = scrapy.Field()
    
    # author
    author = scrapy.Field()
    
    # comment
    comment = scrapy.Field()
    
    # timestamp
    timestamp = scrapy.Field()

    # others