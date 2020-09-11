import scrapy
from ..items import ExtendBookItem


class booksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            bookItem = ExtendBookItem()
            bookItem['姓名'] = book.xpath('./h3/a/@title').extract_first()
            bookItem['价格'] = book.css('p.price_color::text').extract_first()
            bookItem['翻译'] = book.css('p.price_color::text').extract_first()
            yield bookItem
        next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_url:
            # 如果找到下一页的URL，得到绝对路径，构造新的Request 对象
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)