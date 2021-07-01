# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from time import sleep

from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class SeleniumMiddleware(object):

    @classmethod
    def from_crawler(cls, study):
        middleware = cls()
        study.signals.connect(middleware.spider_opened, signals.spider_opened)
        study.signals.connect(middleware.spider_closed, signals.spider_closed)
        return middleware

    def spider_opened(self, spider):
        CHROMEDRIVER_PATH = './chromedriver.exe'
        WINDOW_SIZE = "1920,1080"

        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        #chrome_options.add_argument("disable-gpu")
        chrome_options.add_argument(f"--window-size={WINDOW_SIZE}")
        #chrome_options.add_argument("User-Agent:  Mozilla/5.0 (Macintosh")

        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
        self.driver = driver
        # date = self.driver.find_element_by_xpath('//*[@id="collapse-content"]/ytd-search-filter-group-renderer[1]')
        # click_list_1 = date.find_elements_by_id('endpoint')
        # click_list_1.click()
        # sleep(10)
        spider.logger.info('Spider opened: %s' % spider.name)



    def spider_closed(self, spider):
        self.driver.close()

    def process_request(self, request, spider):
        self.driver.get(request.url)
        #여기다 selenium코드 작성

        # element = self.driver.find_element_by_name("search_query")
        # element.send_keys("항만 뉴스")
        # element.submit()
        # sleep(4)
        self.driver.find_element_by_xpath('//*[@id="container"]/ytd-toggle-button-renderer/a').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="collapse-content"]/ytd-search-filter-group-renderer[1]/ytd-search-filter-renderer[3]/a').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="container"]/ytd-toggle-button-renderer/a').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="collapse-content"]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a').click()
        sleep(1)

        body = to_bytes(text=self.driver.page_source)
        sleep(1)

        return HtmlResponse(url=request.url, body=body, encoding='utf-8', request=request)


class StudySpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class StudyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        ChildProcessError
        spider.logger.info('Spider opened: %s' % spider.name)
