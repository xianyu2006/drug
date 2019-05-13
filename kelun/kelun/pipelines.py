# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv    #这里是将数据保存为csv格式
import os

class KelunPipeline(object):
   
    def __init__(self):
        self.f = open('kl.csv','a+',encoding='utf-8',newline="")#这里的''写错了，导致一直出问题，要照抄
        self.writer = csv.writer(self.f)
        self.writer.writerow(['名称','价格']) #这里没有加[]时，写入的数据都在第一行，没有分行

    def process_item(self, item, spider):
        for titles,lins in zip(item['name'],item['price']):

            self.writer.writerow([titles,lins])
        return item #这里缩进了四个空格，导致写入csv时只写入第一行数据，后面的数据就没有导入

    def close_spider(self,spider):
        self.writer.close()
        self.f.close()

        #之后在settings里打开pipline