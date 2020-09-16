# _*_ coding:utf-8 _*_
# -*- coding: utf-8 -*-
import pytest
from _pytest import unittest
from selenium import webdriver
import time
import allure



@allure.testcase("https:/ /www. baidu. com的搜索功能")
# @pytest.mark.parametrize('test_data1',['allure','pytest','unittest'])
def test_steps_demo():
    with allure.step('step one:打开浏览器输入百度网址'):
        driver = webdriver.Chrome(executable_path='C:\Users\Administrator\PycharmProjects\seleniuma\driver\chromedriver.exe')
    with allure.step("打开百度"):
        driver.get('https://www.baidu.com')
    with allure.step('step two: 在搜索栏输入allure,并点击百度一下'):
        driver.find_element_by_id('kw').send_keys("可乐")
        time. sleep(2)
        driver. find_element_by_id('su').click()
        time. sleep(5)
    with allure. step('step three: 截图保存到项目中'):
        driver.save_screenshot("1.png")
        # f= open(' ./ result/b.png', 'rb'). read( )
        allure. attach. file("1.png", attachment_type=allure.attachment_type.PNG)
        # allure. attach( '<head></head><body>首页</body>','Attach with HTML type',
        #                 allure. attachment_type.HTML)
    with allure.step('step four:关闭浏览器，退出'):
        driver.quit()