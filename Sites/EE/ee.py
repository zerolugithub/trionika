# coding: utf8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string
import allure
import pytest
from selene.conditions import text
from selene.api import *
import time

from General_pages.order_steps import random_mail

@allure.step('Нажимаем на главной странице кнопку Order')
def proceed_to_order():
    print 'Create order on EE'
    s(by.text('Order Now')).click()

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    #s('#header > nav > div.navbar-fixed-top.holder > ul > li:nth-child(5) > a').click()
    s(by.xpath('//*[@id="header"]/nav/div[1]/ul/li[5]/a/span')).click()
    browser.driver().switch_to.window(browser.driver().window_handles[1])
    browser.driver().maximize_window()