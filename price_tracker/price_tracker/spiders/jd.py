# -*- coding: utf-8 -*-
import scrapy
from price_tracker.items import PriceTrackerItem
from price_tracker.jingdong import jd_api
import datetime
from price_tracker.settings import JD_ITEM_DIR
from price_tracker.pipelines import PriceTrackerPipeline
from price_tracker.settings import db_config


class JdSpider(scrapy.Spider):
    name = 'jd'

    def __init__(self):
        self.item = dict()
        with open(JD_ITEM_DIR, 'r', encoding='utf-8') as jd_items:
            for item in jd_items:
                print(item)
                self.item[item.split(': ')[0]] = item.split(': ')[1].rstrip('\n')
                # print(self.item)

    # allowed_domains = ['jingdong.com']
    # start_urls = ['http://jingdong.com/']
    def start_requests(self):
        for item_id, name in self.item.items():
            url = 'https://item.jd.com/{id}.html'.format(id=item_id)
            yield scrapy.Request(url=url, callback=self.parse, encoding='utf-8')

    def parse(self, response):
        item = PriceTrackerItem()
        item['id'], item['price'] = jd_api.get_jd_id_price(url=response.url)
        item['name'] = self.item[item['id']]
        if not item['name']:
            item['name'] = self.item[item['id']]
        item['time'] = datetime.datetime.now().date()
        item['site'] = 'jd'
        yield item