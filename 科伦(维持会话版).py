# -*- coding: utf-8 -*-
#用session维持会话，以免经常换cookies      2019.4.25

import requests
from lxml import etree
import codecs
from requests.exceptions import RequestException
import csv
import time
#写入csv抬头
with open('kelun00.csv','ab+') as fp:
    fp.write(codecs.BOM_UTF8)   #这里是下划线
fp= open('kelun00.csv','a+',errors='ignore',newline="",encoding='utf-8') 
writer = csv.writer(fp)
writer.writerow(['名称','价格'])
#维持会话
s = requests.Session()
post_url = 'http://klyp.kelunyy.com/login.html'    #这里是post的网页
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
           }
formdata = {'username':'8888',      #填入用户名
            'userpass':'0000',      #填入密码
            'do':'login'
             }
r = s.post(url=post_url,headers=headers,data = formdata)
#维持会话后，在登陆情况下访问其他页面
get_url = ["http://klyp.kelunyy.com/goods-filter-1247-0-0-0-0-1-{}.html".format(i) for i in range(1,215,1)]  #这里是get的网页
for url in get_url:
    its = s.get(url ,headers = headers)

    selector = etree.HTML(its.text)
    infos = selector.xpath('.//*[@id="pro_list1"]//li')
    for info in infos:
        name =info.xpath('//p[1]/*[@class="blue"]//text()')     
        price =info.xpath('//li/p/span//text()')
        #time.sleep(1)
    for n,p in zip (name,price):
        ps = p[1:]
        
        writer.writerow([n,ps])
            
fp.close()
