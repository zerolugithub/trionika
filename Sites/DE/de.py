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
    print 'Create order on DE'
    s(by.xpath('//button[@class="btn red button-submit-calc-order"]')).click()

@allure.step('Нажимаем на главной странице кнопку Inquiry')
def click_inquiry_button():
    time.sleep(2)
    print 'Create inquiry on DE'
    browser.driver().execute_script(("window.scrollTo(0, document.body.scrollHeight);"))
    s('body > div.footer-all > div.order > div > a').click()

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s(by.text('Sign in')).click()

@allure.step('Нажимаем на главной странице кнопку Discount')
def click_discount_button_on_header():
    s(by.xpath('//button[@class="btn"]')).click()