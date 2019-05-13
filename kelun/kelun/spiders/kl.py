# -*- coding: utf-8 -*-
import scrapy
import sys                                                                 #我用的vscode，这里就要加这两行代码，否则导入item不成功
sys.path.append(r'C:\Users\Administrator\AppData\Roaming\Code\User\kelun')   #我用的vscode，这里就要加这两行代码，否则导入item不成功
from kelun.items import KelunItem    #这里是导入Item


class KlSpider(scrapy.Spider):
    name = 'kl'       #项目名
    allowed_domains = ['kelunyy.com']
    start_urls = ['http://klyp.kelunyy.com/login.html']

    def parse (self,response):
        login_url = 'http://klyp.kelunyy.com/login.html'
        formdata = {'username':'.....',
                     'userpass':'.....',
                      'do':'login'

                     }         #formada里如果有变化的表单数据，可以利用xpath等方式解析这个参数（scrapy可以自动解析参数，不用手写xpath）
             #这里是发送post请求（FormRequest）
        yield scrapy.FormRequest(login_url,
                                formdata = formdata,
                                callback = self.parse_login)   #这里最开始模拟登录没有成功是setting.py的设置没有改。callback这个是回调函数，将上面的函数回调给parse_login这个函数
                                       

    def parse_login(self, response):
        menber_url = 'http://klyp.kelunyy.com/goods-filter-0-0-0-0-0-1-1.html'
        yield scrapy.Request(menber_url,callback=self.parse_menber

        )    #这里就携带了cookies访问需要解析的网页，要在settings改请求头

    def parse_menber(self,response):

        #with open('kl.html','wb') as f:  #这里是打印登陆后的网页，看是否登录成功
            #f.write(response.body)
            
        infos =  response.xpath('//*[@id="pro_list1"]//li')
        for info in infos:
            item = KelunItem()
            item['name'] =info.xpath('.//p[1]/*[@class="blue"]/text()').extract()       
            item['price'] = info.xpath('.//p/*[@class="red"]/text()').extract()   #这里定位解析错误，就没有提取price成功
            

            yield item
        #实现翻页功能
        nextpage = response.xpath('/html/body/div[4]/div/div[5]/a[10]/@href').extract()
        if nextpage:
            yield scrapy.http.Request("http://klyp.kelunyy.com/"+nextpage[0],callback=self.parse_menber)

        
        
