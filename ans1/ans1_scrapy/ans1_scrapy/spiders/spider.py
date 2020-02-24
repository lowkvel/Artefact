# -*- coding: utf-8 -*-
import scrapy
import json
from ans1_scrapy.items import Ans1ScrapyItem

class Ans1ScrapySpider(scrapy.Spider):
    
    # the name of the spider
    name = 'ans1_scrapy_spider'
    
    # pages to crawl, 5 for now
    max_pages = 5
    
    # allowed domains for scrapy
    allowed_domains = ['item.jd.com']
    
    # comment pages for scrapy
    url_pre = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=1384071&score=0&sortType=5&page='
    url_page_number = 0
    url_suf = '&pageSize=10&isShadowSku=0&fold=1'
    start_urls = (url_pre + str(url_page_number) + url_suf,)
    
    def parse(self, response):
        
        # fetch the comments section for current page only
        jd_comments = json.loads(response.text.lstrip('fetchJSON_comment98(').rstrip(');'))['comments']
        
        # extract the required data
        item = Ans1ScrapyItem()
        for i in jd_comments:
            item['id'] = i['id']
            item['author'] = i['nickname']
            item['comment'] = i['content']
            item['timestamp'] = i['creationTime']
            yield item
    
        # update pages_number, 5 pages for now
        if self.url_page_number < self.max_pages:
            self.url_page_number += 1
            yield scrapy.Request(self.url_pre + str(self.url_page_number) + self.url_suf, callback=self.parse, dont_filter=True)
            
            
            
            
            
            
            
            
            