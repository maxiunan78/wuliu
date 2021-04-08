#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from  time import sleep
import os

class Page(object):
    """基础类，用于页面的继承"""

    base_url = 'http://172.18.8.221:8180'

    def __init__(self, selenium_driver,base_url=base_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    # def on_page(self):
    #     print "当前页面:"  + str(self.driver.current_url)
    #     return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        print url
        self.driver.get(url)
        # assert self.on_page(), 'Did not land on %s' %url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)





class LoginPage(Page):

    url = "/api/login"

    username_loc = (By.XPATH,"//input[@name='mobile']")
    password_loc = (By.XPATH,"//input[@name='password']")
    submit_loc = (By.XPATH,"//button[@type='button']")

    # add_loc = (By.CSS_SELECTOR,"#app-container > div.filter-container > button:nth-child(6)")

    #Action
    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()



class Contract_managementPage(Page):
   # 合同管理页面
    url = '/api/home'
    frame_loc = ("/api/carrierContract/index")
    add_loc = (By.XPATH,"//div[1]/button[2]")
    click1_loc = (By.XPATH,"//*[@id='menuList']/li[5]/div/span")
    click2_loc = (By.XPATH,"//*[@id='menuList']/li[5]/ul/li/ul/li[2]/span")
    input_projectnum =(By.XPATH,"//*[@id='app-container']/div[4]/div/div[2]/div/div/div/form/div[1]/div[1]/div/div/div[1]/input")
    box_loc = (By.XPATH,"//*[@id='app-container']/div[4]/div/div[2]/div/div/div/form/div[1]/div[2]/div/div/div/div/input")
    boxinput_loc =(By.XPATH,"/html/body/div[5]/div[1]/div[1]/ul/li[1]/span")
    main_goods_loc = (By.XPATH,"//*[@id='app-container']/div[4]/div/div[2]/div/div/div/form/div[1]/div[4]/div/div/div[1]/input")
    loadfile_loc = (By.XPATH,"//*[@id='app-container']/div[4]/div/div[2]/div/div/div/form/div[2]/div[1]/div/div/div[1]/div")

    def click1(self):
        self.find_element(*self.click1_loc).click()

    def click2(self):
        self.find_element(*self.click2_loc).click()

    # def switch_frame(self):
    #     sleep(2)
    #     e = self.driver.find_element_by_id(self.frame_loc)
    #     WebDriverWait(self.driver, 10).until(ec.frame_to_be_available_and_switch_to_it(e))
        # self.driver.switch_to_frame(e)




    def add(self):

        # self.switch_frame()
        e = self.driver.find_element_by_id(self.frame_loc)
        WebDriverWait(self.driver, 10).until(ec.frame_to_be_available_and_switch_to_it(e))
        self.find_element(*self.add_loc).click()

    def write_project_num(self):
        self.find_element(*self.input_projectnum).send_keys("23232")

    def click_box(self):
        self.find_element(*self.box_loc).click()
        self.find_element(*self.boxinput_loc).click()

    def main_goods_input(self):
        self.find_element(*self.main_goods_loc).send_keys(u"煤炭")

    def loadfile(self):
        self.find_element(*self.loadfile_loc).click()
        os.system("C:\Users\Administrator\Desktop\Autolt_1.au3")
