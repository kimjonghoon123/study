# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StudyItem(scrapy.Item):
    date = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    fileimg = scrapy.Field()
    num = scrapy.Field()

