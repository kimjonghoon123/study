# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import MySQLdb
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import ImagesPipeline


class StudyPipeline():
    def process_item(self, spider):
        return

# class MySQLpipeline(object):
#     def open_spider(self, spider):
#         settings = spider.settings
#         params = {
#             'host': settings.get('MYSQL_HOST', 'localhost'),
#             'db': settings.get('MYSQL_DATABASE', 'scraping'),
#             'user': settings.get('MYSQL_USER', ''),
#             'passwd': settings.get('MYSQL_PASSWORD', ''),
#             'charset': settings.get('MYSQL_CHARSET', 'utf8mb4'),
#         }
#
#         self.conn = MySQLdb.connect(**params)
#         self.c = self.conn.cursor()
#         self.c.execute('''
#             CREATE TABLE IF NOT EXISTS items(
#                 id INTEGER NOT NULL AUTO_INCREMENT,
#                 title CHAR(200) NOT NULL,
#                 PRIMARY KEY (id)
#                 )
#             ''')
#         self.conn.commit()
#
#     def close_spider(self, spider):
#         self.conn.close()
#
#     def procese_items(self, item, spider):
#         self.c.execute('INSERT INTO items (title) VALUES (%(title)s)', dict(item))
#         self.conn.commit()
#
#         return item