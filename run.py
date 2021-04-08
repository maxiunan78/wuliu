#!/usr/bin/env python
#-*- coding:utf-8 -*-
import selenium
from selenium.webdriver import Remote
from selenium.webdriver import Chrome
from  selenium import webdriver
from  test import case as ca
from time import sleep
import unittest
#
# def tryf():
    # driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',
    #                 desired_capabilities={'platform':'ANY',
    #                                     'browserName':'chrome',
    #                                     'version':'',
    #                                     'javascriptEnabled':'True'}
    #             )
    #
    # driver.get('http://www.baidu.com')
    # driver.find_element_by_id("kw").send_keys("remote")
    # driver.find_element_by_id("su").click()


    # driver = Chrome(executable_path=r'E:\apk\chromedriver\chromedriver_win32')
    # global driver
    # driver = Chrome()
    # driver.get('http://172.18.8.221:8180/api/login')
    # driver.find_element_by_xpath("//input[@name='mobile']").send_keys("wl003")
    # driver.find_element_by_xpath("//input[@name='password']").send_keys("qwer1234")
    # driver.find_element_by_xpath(("//button[@type='button']")).click()
    #
    # driver.implicitly_wait(10)
    # driver.find_element_by_id("su
    # driver = webdriver.Firefox()
    # driver.get("htttp://www.youdao.com")

    # driver.quit()
#
# if __name__== '__main__':
#     tryf()

# class Testindexpage(unittest.TestCase):
#
#         def setUp(self):
#                 self.driver = Chrome()
#                 self.driver.get('http://172.18.8.221:8180/api/login')
#                 self.driver.implicitly_wait(4)
#                 print ("test start!")
#         def test_case(self):
#             self.driver.implicitly_wait(4)
#             self.driver.find_element_by_xpath("//input[@name='mobile']").send_keys("wl003")
#             self.driver.find_element_by_xpath("//input[@name='password']").send_keys("qwer1234")
#             self.driver.find_element_by_xpath("//button[@type='button']").click()
#             self.driver.implicitly_wait(10)
#             e = self.driver.find_element_by_xpath("//span[text()='首页']")
#             self.assertIsNotNone(e)
#         def tearDown(self):
#                 print("test end")
#                 self.driver.quit()
#
#
# if __name__=="__main__":
#         unittest.main()

def main():
    try:
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        username = 'wl003'
        password = 'qwer1234'
        ca.test_user_login(driver,username,password)
        sleep(3)
        ca.test_contract_management(driver)
        sleep(2)
        # text = driver.find_element_by_xpath("//*[@id='tab-1']/span/span").text
        # print text
        # sleep(2)
        # assert (text == u'首页'),"登录失败"
    finally:
        print "111"
        driver.close()

if __name__ == '__main__':
    main()