#!/usr/bin/env python
#-*- coding:utf-8 -*-
import po_model
def test_user_login(driver, username, password):

    login_page = po_model.LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()


def test_contract_management(driver):

    Contract_managementPage = po_model.Contract_managementPage(driver)
    Contract_managementPage.open()
    Contract_managementPage.click1()
    Contract_managementPage.click2()
    # Contract_managementPage.switch_frame()
    Contract_managementPage.add()
    Contract_managementPage.write_project_num()
    Contract_managementPage.click_box()
    Contract_managementPage.main_goods_input()
    Contract_managementPage.loadfile()