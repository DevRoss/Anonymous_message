# -*- coding: utf-8 -*-
from price_tracker.settings import db_config
import pymysql


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PriceTrackerPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(**db_config)

    def process_item(self, item, spider):
        try:
            with self.conn.cursor() as cursor:
                sql = 'insert into item(site, id, name, price, time) values(%s, %s, %s, %s ,%s)'
                cursor.execute(sql, (item['site'], item['id'], item['name'], item['price'], item['time']))
                self.conn.commit()
                return item
        except Exception as error:
            print(error)

    def close_spider(self, spider):
        self.conn.close()
