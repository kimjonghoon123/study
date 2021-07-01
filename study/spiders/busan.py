import scrapy


class BusanSpider(scrapy.Spider):
    name = 'busan'
    start_urls = ['https://www.busanpa.com/kor/Board.do?mCode=MN0793']

    def parse(self, response):
        start_urls = ['https://www.busanpa.com/kor/Board.do']
        titles = response.xpath('//*[@id="board-wrap"]/table/tbody/tr/td[3]/a/text()').getall()
        hrefs = response.xpath('//*[@id="board-wrap"]/table/tbody/tr/td[3]/a/@href').getall()
        dates = response.xpath('//*[@id="board-wrap"]/table/tbody/tr/td[5]/text()').getall()

        for num, href in enumerate(hrefs):
            a = start_urls[0] + href
            b = dates[num].strip()
            c = titles[num]
            print(a,b,c)