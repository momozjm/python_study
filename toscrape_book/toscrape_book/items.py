# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ToscrapeBookItem(scrapy.Item):
    # define the fields for your item here like:
    姓名 = scrapy.Field()
    价格 = scrapy.Field()
    pass


# 继承：传入父类
class ExtendBookItem(ToscrapeBookItem):
    翻译 = scrapy.Field()
    pass


class Job58CityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    名称 = scrapy.Field()
    薪资 = scrapy.Field()
    福利 = scrapy.Field()
    公司 = scrapy.Field()
    职位类型 = scrapy.Field()
    学历 = scrapy.Field()
    经验 = scrapy.Field()
    地址 = scrapy.Field()
