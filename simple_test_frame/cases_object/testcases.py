#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pages_object.testpage import BaiduLoginPage
from pages_object.testpage import SogouLoginPage
import unittest
import xmlrunner

class WebTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        print ("-----test beginning------")

    @classmethod
    def tearDown(self):
        print ("-----test ending-----")

    def test_baidu_login(self):
        #创建测试对象子类
        bdLogin = BaiduLoginPage()
        #创建断言来判断是否登录成功
        self.assertEqual(0, bdLogin.userLogin('eps2012', '156627150'))

    def test_sogou_login(self):
        sgLogin = SogouLoginPage()
        self.assertEqual(0, sgLogin.userLogin('13917541762', '156627150'))

if __name__ == "__main__":
    testSuites = unittest.TestSuite()
    testSuites.addTest(WebTests('test_sogou_login'))
    #这里使用xml来作为日志输出的文本格式，并保存在本地目录
    runner = xmlrunner.XMLTestRunner(output='c:/test_logs/', verbosity=2)
    runner.run(testSuites)






