# -*- coding: utf-8 -*-
#用xpath解析数据，抓取名称和价格，存入csv,这次爬取全部网页      2019.4.10
#这一版是正确的，可以提取出数据

import requests
import codecs
from lxml import etree
import time
from bs4 import BeautifulSoup
import csv
with open('113.csv','ab+') as fp:
    fp.write(codecs.BOM_UTF8)   #这里是下划线
fp= open('113.csv','a+',errors='ignore',newline="",encoding='utf-8') 
writer = csv.writer(fp)
writer.writerow(['名称','价格'])
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
           'Cookie':}  #此处加上自己的cookie

#for i in range(27):
urls =["http://klyp.kelunyy.com/goods-filter-1247-0-0-0-0-1-{}.html".format(i) for i in range(1,27,1)]

for url in urls:
    html = requests.get(url,headers=headers) 
    selector= etree.HTML(html.text)
    
    infos = selector.xpath('.//*[@id="pro_list1"]//li')
    for info in infos:
        name =info.xpath('//p[1]/*[@class="blue"]//text()')         #//*[@class="blue"]//text()
        price = info.xpath('//li/p/span//text()')
        
    for n,p in zip (name,price):
        ps = p[1:]
        
        writer.writerow([n,ps])
            
fp.close()
 
