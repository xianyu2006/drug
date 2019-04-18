# -*- coding: utf-8 -*-
#用xpath解析数据，抓取名称和价格，存入csv,这次爬取全部网页，用定义函数的方法      2019.4.18

import requests
from lxml import etree
import codecs
from requests.exceptions import RequestException
import csv
import time
#写入表头
with open('li4.csv','ab+') as fp:
        fp.write(codecs.BOM_UTF8)   #这里是下划线
fp= open('li4.csv','a+',errors='ignore',newline="",encoding='utf-8') 
writer = csv.writer(fp)
writer.writerow(['名称','价格'])

#定义函数，获取一页网页的源代码
def get_one_page(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
           'Cookie':'UM_distinctid=169b4d7a3e738f-070df82c5473bd-5f123917-13c680-169b4d7a3e8245; PHPSESSID=14jirih8evps6ivesajehs1r8r; CNZZDATA1275384522=1672243937-1553516935-null%7C1555329891; c_member_id=109224'
        }
        response =requests.get(url,headers=headers)
        if response.status_code ==200:
            print('成功获取源代码')
    except RequestException as e:
        print('获取源代码失败：%s' % e)  
    return response.text

#解析网页内容，并返回结果
def parse_one_page(html):    
    selector= etree.HTML(html)
    infos = selector.xpath('//*[@id="pro_list1"]//li')
    for info in infos:
        yield(
        info.xpath('.//p[1]/a//text()')[0] ,  #这里的错误是少一个逗号
        info.xpath('.//p[6]/span//text()')[0]
        )
#主函数，传入参数
def main():
    url ="http://klyp.kelunyy.com/goods-filter-1247-0-0-0-0-{}.html".format(i)
    html = get_one_page(url)
    dy = parse_one_page(html)
    for info in dy:
        writer.writerow(info)
        print(info)          #这里将字典写入csv中的解决办法是yield后面的{}改为（）,同时将
#遍历所有网页      
if __name__ == '__main__':
    for i in range(215):
        main()    #这里面是空的，没有参数
        time.sleep(1)

