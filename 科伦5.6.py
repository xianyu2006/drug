# -*- coding: utf-8 -*-
#用xpath解析数据，抓取名称和价格，存入csv,这次爬取全部网页，用定义函数的方法      2019.4.14

import requests
from lxml import etree
import codecs
from requests.exceptions import RequestException
import csv
import time
#写入表头
with open('li5.6.csv','ab+') as fp:
        fp.write(codecs.BOM_UTF8)   #这里是下划线
fp= open('li5.6.csv','a+',errors='ignore',newline="",encoding='utf-8') 
writer = csv.writer(fp)
writer.writerow(['名称','价格'])

#定义函数，获取一页网页的源代码
def get_one_page(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
           'Cookie':''
        }
        response =requests.get(url,headers=headers)
        if response.status_code ==200:
            print('成功获取源代码')
    except RequestException as e:
        print('获取源代码失败：%s' % e)  
    return response.text

#解析网页内容，并返回结果
def parse_one_page(html):    #这里的content就是html.text
    
    selector= etree.HTML(html)
    infos = selector.xpath('//*[@id="pro_list1"]//li')
    #books = []
    for info in infos:
        yield(
        info.xpath('.//p[1]/a//text()')[0] ,  #这里的错误是少一个逗号
        info.xpath('.//p[6]/span//text()')[0]
        )
#主函数
def main():
    url ="http://klyp.kelunyy.com/goods-filter-1247-0-0-0-0-{}.html".format(i)
    html = get_one_page(url)
    number = etree.HTML(html).xpath('//*[@id="pro_list1"]//li//p[1]/a//text()')
    #这里的作用是判断每页是否采集了20个药品，进而好知道到底是那页的数据没有采集够
    try:
        if len(number)==20:
            print("第%s页采集正常"%i)
    except Exception as e:
        print("第%s页采集不正常"%e)  
  
    dy = parse_one_page(html)   
    for info in dy:
        
        writer.writerow(info)
                 #这里将字典写入csv中的解决办法是yield后面的{}改为（）,同时将
#遍历所有网页      
if __name__ == '__main__':
    for i in range(1,10):
        main()
        time.sleep(1)

