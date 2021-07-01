# -*- coding: utf-8 -*-
import scrapy
from study.items import StudyItem

class YeosuSpider(scrapy.Spider):
    name = 'yeosu'
    start_urls = ['https://www.ygpa.or.kr/kr/release_information/release_information/gonggo']

    def parse(self, response):
        start_urls = ['https://www.ygpa.or.kr/kr/release_information/release_information/gonggo']
        href = response.xpath('//*[@id="bbsForm"]/table/tbody/tr/td/a/@href').getall()
        titles = response.xpath('//*[@id="bbsForm"]/table/tbody/tr/td/a/text()').getall()
        createdate = response.xpath('//*[@id="bbsForm"]/table/tbody/tr/td[3]/text()').getall()
        for num, title in enumerate(href):
            doc = StudyItem()
            a = start_urls[0] + title
            b = createdate[num].strip().replace("\r", "").replace("\n", "").replace("\t", "")
            c = titles[num]
            print("주소 : ", a, "생성일 : ", b, "제목 : ", c)
            doc["link"] = a
            doc["title"] = c
            doc["date"] = b
            yield doc




