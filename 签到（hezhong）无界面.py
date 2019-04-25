# -*- coding: utf-8 -*-
#这次的功能是每天可以自动登录合纵网站，并自动签到，不用每天手动签到
import requests
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()   #这里的错误在最后少一个括号
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#驱动路径
path = r'D:\Users\Administrator\Anaconda3\Scripts\chromedriver.exe'
#创建浏览器对象
browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)


browser.get('https://www.hezongyy.com/jifen')
browser.find_element_by_xpath('/html/body/div[1]/div/div/a[1]').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="username"]').send_keys('xianyu2006')  #这最开始的错误是输入不了登录名，应该是by_xpath，而不是by_id
time.sleep(3)
browser.find_element_by_xpath('//*[@id="password"]').send_keys('')  #这里填写密码
browser.find_element_by_xpath('//*[@id="form"]/div/div/div/a').click()
time.sleep(3)
browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/div[3]/a[1]').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="qiandao"]').click()
time.sleep(5)
browser.save_screenshot('kelun5.png')
browser.quit()
