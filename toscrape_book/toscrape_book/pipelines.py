# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class PriceConverterPipeline(object):
    # 英镑兑换人民币汇率
    exchange_rate = 8.5309

    def process_item(self, item, spider):
        # 提取item的price 字段（如￡53.74）
        # 去掉前面英镑符号￡，转换为float 类型，乘以汇率。 切片[1:] 从索引1切到末尾，字符串也可以
        price = float(item['价格'][1:]) * self.exchange_rate

        # 保留2 位小数，赋值回item的price 字段
        # Python的字符串格式化有两种方式:%格式符方式，format方式
        # %后面是格式化内容，.2是小数点两位, f是转为浮点数
        item['价格'] = '￥%.2f' % price

        return item


class DuplicatesPipeline(object):

    def __init__(self):
        # set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据。和es6的set()去重一样
        self.book_set = set()

    def process_item(self, item, spider):
        name = item['姓名']
        if name in self.book_set:
            # 抛出DropItem异常，将item抛弃
            raise DropItem("Duplicate book found: %s" % item)

        self.book_set.add(name)
        return item
