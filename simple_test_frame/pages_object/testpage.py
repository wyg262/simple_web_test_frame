#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base_page_object.basepage import BasePage

class BaiduLoginPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        self.baseUrl = 'https://www.baidu.com'
        #封装需要的页面元素
        #首页登录按钮xpath
        self.homePageloginButton = ["xpath", "//*[@id='u1']/a[@name='tj_login']"]
        #弹窗从扫描切换到“用户名登录”按钮
        self.userNameloginButton = ["xpath", "//*[@id='TANGRAM__PSP_10__footerULoginBtn']"]
        #弹窗“手机/邮箱/用户名”输入框
        self.userNameInput = ["xpath", "//*[@id='TANGRAM__PSP_10__userName']"]
        #弹窗“密码”输入框
        self.userPasswordInput = ["xpath", "//*[@id='TANGRAM__PSP_10__password']"]
        #弹窗“登录”按钮
        self.userLoginButton = ["xpath", "//*[@id='TANGRAM__PSP_10__submit']"]
        #登录后页面展示现实账号
        self.logged_username = ["xpath", "//*[@id='s_username_top']/span[@class='username']"]

        #定义用户登录方法
    def userLogin(self, username, password):
        self.open_page(self.baseUrl)
        self.click_element(self.homePageloginButton)
        self.click_element(self.userNameloginButton)
        self.send_key_to_element(self.userNameInput, username)
        self.send_key_to_element(self.userPasswordInput, password)
        self.click_element(self.userLoginButton)
        username = self.find_element(self.logged_username).get_attribute()
        res = 0 if username == "eps2012" else 1
        self.close_page()
        return res

class SogouLoginPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        self.baseUrl = 'https://pinyin.sogou.com/'
        #首页登录按钮链接
        self.homePageloginButton = ["xpath", "//*[@id='user_info']/ul/li[2]/div[1]/a"]
        #弹窗用户名输入框
        self.userNameInput = ["xpath", "//*[@onfocus='psfocus(1);']"]
        #弹窗密码输入框
        self.userPasswordInput = ["xpath", "//*[@onfocus='psfocus(3);']"]
        #弹窗登录按钮
        self.loginBtn = ["xpath", "//*[@class='btn_bar']/table/tbody/tr/td[2]/input"]
        #登录完成页面用户名
        self.loggedUsername = ["xpath", "//*[@id='user_info']/ul/li[2]/div[1]/a"]

    def userLogin(self, username, password):
        self.open_page(self.baseUrl)
        self.click_element(self.homePageloginButton)
        self.send_key_to_element(self.userNameInput, username)
        self.send_key_to_element(self.userPasswordInput, password)
        self.click_element(self.loginBtn)
        self.wait_time()
        name = self.find_element(self.loggedUsername).text
        if username in name:
            res = 0
        else:
            res = 1
        self.wait_time()
        self.close_page()
        return res


























