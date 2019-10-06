#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def wait_time(self):
        time.sleep(5)

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def close_page(self):
        self.driver.quit()

    def find_element(self, selector):
        method = selector[0]
        value = selector[1]
        #通过id, name, classname, xpath方式来定位需要操作的元素并返回，使用WebDriverWait防止元素未定位完成就执行后续的操作
        if method in 'id' or 'name' or 'class' or 'xpath':
            if method == 'id':
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, value)))
            elif method == 'name':
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, value)))
            elif method == 'class':
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            elif method == 'xpath':
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, value)))
            else:
                print ('no element found')
            return element
        else:
            print ('search method error')

    #定位元素并模拟输入
    def send_key_to_element(self, selector, value):
        element = self.find_element(selector)
        try:
            element.send_keys(value)
        except Exception:
            print ('input error occurred')

    #定位元素模拟点击
    def click_element(self, selector):
        element = self.find_element(selector)
        try:
            element.click()
        except Exception:
            print ('click element error')








