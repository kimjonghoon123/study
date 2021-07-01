import scrapy
from selenium import webdriver
from time import sleep
from study.items import StudyItem


class YoutuSpider(scrapy.Spider):
    name = 'imgs'
    start_urls = ['https://www.youtube.com/results?search_query=%ED%95%AD%EB%A7%8C%EB%89%B4%EC%8A%A4']
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'study.middlewares.SeleniumMiddleware': 100
        }
    }

    def parse(self, response):
        imgsrcs = response.xpath('//div[@id="contents"]//yt-img-shadow/img')
        for img in imgsrcs:
            img_url = img.xpath('/@src').extract_first()
            print("이미지 src : ", img_url)
            yield {'image_urls': [img_url]}  # 주석  ㅎㅇㅎㅇ
