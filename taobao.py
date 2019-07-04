# # -*- coding: UTF-8 -*-
# 测试淘宝抢单 功能

import os
import requests
import importlib
from PIL import Image
import requests
import img2pdf
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import yaml
class taobaoModel(object):
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        config = {}
        with open(base_path + "/config.yaml") as f:
            config = yaml.load(f)
        driverPath = config['chromePath']
        weiboName = config['weiboUsername']
        weiboPwd = config['weiboPassword']
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-automation'])
        browser = webdriver.Chrome(driverPath, options=options)
        browser.get("https://www.taobao.com")
        browser.find_element_by_link_text("亲，请登录").click()
        time.sleep(10)
        browser.find_element_by_link_text("密码登录").click();
        time.sleep(10)
        browser.find_element_by_class_name("weibo-login").click();
        time.sleep(10)
        browser.find_element_by_name("username").send_keys(weiboName);
        time.sleep(10)
        browser.find_element_by_name("password").send_keys(weiboPwd);
        time.sleep(10)
        browser.find_element_by_class_name("W_btn_g").click();
        time.sleep(20)
        self.browser = browser

    def parse(self,html):
        Content = BeautifulSoup(html.content, 'html.parser')
        return Content

    def buy(self):
        self.browser.get("https://cart.taobao.com/cart.htm")
        if self.browser.find_element_by_id("J_SelectAll1"):
            self.browser.find_element_by_id("J_SelectAll1").click()
        time.sleep(2)
        self.browser.find_element_by_link_text("结 算").click();
        time.sleep(10)
        self.browser.find_element_by_link_text("提交订单").click();
        time.sleep(10)
        return

    def getUserinfo(self):
        self.browser.get("https://rate.taobao.com/myRate.htm")
        self.browser.find_element_by_link_text("我的购物车").click();
        return


if __name__ == '__main__':
    taobaoUserSession = taobaoModel()
    taobaoUserSession.buy()
    taobaoUserSession.getUserinfo()
