# -*- coding: utf-8 -*-
import time

import scrapy
from ..items import Job58CityItem


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['58.com']
    start_urls = ['https://nj.58.com/caiwu/pn1/']

    # 解析html内容
    def parse(self, response):
        # //E：选中文档中的所有E，无论在什么位置。
        for each in response.xpath("//ul[@id='list_con']/li"):
            item = Job58CityItem()
            # E/text()：选中E的文本子节点。
            item['名称'] = each.xpath(".//span[@class='name']/text()").extract()[0]
            money_list = each.xpath(".//p[@class='job_salary']/text()").extract()
            money = "未知"
            if len(money_list) > 0:
                money = money_list[0]
            item['薪资'] = money
            span = each.xpath(".//div[@class='job_wel clearfix']/span")
            item['福利'] = []
            for i in span:
                item['福利'].append(i.xpath("./text()").extract()[0])
            item['公司'] = each.xpath(".//div[@class='comp_name']/a/text()").extract()[0]
            item['职位类型'] = each.xpath(".//span[@class='cate']/text()").extract()[0]
            item['学历'] = each.xpath(".//span[@class='xueli']/text()").extract()[0]
            item['经验'] = each.xpath(".//span[@class='jingyan']/text()").extract()[0]
            item['地址'] = each.xpath("//span[@class='address']/text()").extract()[0]
            yield item
        next_url = response.css('div.pagesout a.next::attr(href)').extract()[0]
        if next_url:
            yield scrapy.Request(next_url, callback=self.parse)
