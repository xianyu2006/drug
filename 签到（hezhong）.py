# -*- coding: utf-8 -*-
#这次的功能是每天可以自动登录合纵网站，并自动签到，不用每天手动签到
import requests
import time 
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.hezongyy.com/jifen')
driver.find_element_by_xpath('/html/body/div[1]/div/div/a[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="username"]').send_keys('xianyu2006')  #这最开始的错误是输入不了登录名，应该是by_xpath，而不是by_id
time.sleep(3)
driver.find_element_by_xpath('//*[@id="password"]').send_keys('')
driver.find_element_by_xpath('//*[@id="form"]/div/div/div/a').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/div[3]/a[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="qiandao"]').click()
time.sleep(5)
