# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:41:55 2021

@author: Emre Kaan
"""

import scrapy
import time
from scrapy_hurriyet.items import ScrapyHurriyetItem

class HurriyetSpyder(scrapy.Spider):
    name="news"
    start_urls =[
        "http://www.haberler.com/arsiv/10-02-2021/ekonomi/s1/"       
        ]
    
    date = ""
    tag = ""
        
    def parse(self,response):
        self.getPropertiesFromLink(response.url)
        pages = response.xpath("/html/body/div[1]/div[2]/div[3]/div/div[2]/div/a/@href").extract()
        pages.pop(0)
        pages = pages[:-1]
        for i in range(len(pages)):
            pages[i] = "https://www.haberler.com" + pages[i]
        pages.insert(0,response.url)
        for p in pages:
            yield scrapy.Request(p, callback=self.handlePage)

        
    def handlePage(self,response):
        news_contents =  response.xpath("//div[@class='box boxStyle color-finance']/a/@href").extract()
        for news in news_contents:
            yield scrapy.Request(news, callback = self.getNewContent)
            
        
            
    def getNewContent(self,response):      
        paragraphs = response.xpath("//*[@id='detaySol']/div[1]/article/div[4]/p/text()").extract()      
        text = ""
        for p in paragraphs:
            if p is None or  p is "":
                continue
            else:
                text = text+p
                
        item = ScrapyHurriyetItem()
        item['date'] = str(self.date)
        item['category'] = str(self.tag)
        item['content'] = str(text)
        yield item
                
    def getPropertiesFromLink(self,response):
        parts = response.split("/")
        self.date = parts[4]
        self.tag = parts[5]
        

        
                    

        


    