# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field 

class ScrapyHurriyetItem(scrapy.Item):
    date = scrapy.Field()
    category = scrapy.Field()
    content = scrapy.Field()
    task_id = scrapy.Field()
    _id = scrapy.Field()