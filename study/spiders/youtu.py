import urllib.request

import scrapy
from selenium import webdriver
from time import sleep
from study.items import StudyItem
import urllib.request
import wget

class YoutuSpider(scrapy.Spider):
    name = 'youtu'
    start_urls = ['https://www.youtube.com/results?search_query=%ED%95%AD%EB%A7%8C%EB%89%B4%EC%8A%A4']
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'study.middlewares.SeleniumMiddleware': 100
        }
    }

    def parse(self, response):

        baseurl = ['https://www.youtube.com']
        href = response.xpath('//div[@id="contents"]/ytd-video-renderer/div//h3/a/@href').getall()
        titles = response.xpath('//div[@id="contents"]/ytd-video-renderer/div//h3/a/@title').getall()
        musics = response.xpath('//*[@id="thumbnail"]/yt-img-shadow/img/@src').getall()
        print(musics)
        for num, a in enumerate(titles):
            doc = StudyItem()
            titles = a
            b = musics[num]
            c = baseurl[0] + href[num]
            doc["title"] = a
            doc["link"] = c
            doc["fileimg"] = b
            doc["num"] = num+1
            print("[", num, "]이미지 소스 : ", b, "제목 : ", titles, "주소 : ", c)
            filename = 'C:/Users/kjh19/OneDrive/바탕 화면/cmder/study/' + a[:4] + '.jpg'
            print(filename)
            wget.download(b, filename)
            yield doc

        # for elem in srcs:
        #     img_url = elem.xpath("@src").extract_first()
        #     print(img_url)
        #     yield {'image_urls': [img_url]}
        # for num, title in enumerate(titles):
        #     a = baseurl[0] + href[num]
        #     c = title
        #     print("주소 : ", a, "제목 : ", c, "이미지 src : ")

    # def parse_img(self, response):
    #
    #     pass
    #     # for elem in imgsrcs:
    #     #
    #     #     img_url = elem
    #     #     yield StudyItem(file_urls=[img_url])
