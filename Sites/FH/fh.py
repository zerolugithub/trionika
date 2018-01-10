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

from General_pages import modals
from General_pages.order_steps import random_mail

@allure.step('Нажимаем на главной странице кнопку Order')
def proceed_to_order():
    print 'Create order on FH'
    s(by.text('Order Now')).click()

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s('body > div.navbar.transparent.navbar-inverse.navbar-fixed-top > div > div.navbar-top > div > ul > li:nth-child(2) > a').click()
    #browser.driver().close()
    time.sleep(1)
    browser.driver().switch_to.window(browser.driver().window_handles[1])
