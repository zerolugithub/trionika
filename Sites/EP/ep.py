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
    print 'Create order on EP'
    s(by.xpath('//a[@class="place-order"]')).click()
    # s('body > div.navigation > div > a.order').click()

@allure.step('Нажимаем на главной странице кнопку Inquiry')
def click_inquiry_button():
    print 'Create inquiry on EP'
    browser.driver().execute_script(("window.scrollTo(0, document.body.scrollHeight);"))
    s(by.xpath('//a[@href="/inquiry.html"]')).click()

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s(by.xpath('//a[@class="signin"]')).click()

@allure.step('Устанавливаем рандомный Deadline')
def choice_deadline():
    n = random.randint(0, 8)
    deadline_list = ['1235', '1236', '1237', '1202', '1203','1204', '1207', '1211', '1215' ]
    deadline = deadline_list[n]
    s(by.xpath('//input[@name="deadline"][@value="%s"]/..'%deadline)).click()
    deadline_dict = { '1235':'3Hours', '1236':'6Hours', '1237':'12Hours', '1202':'24Hours', '1203':'2Days','1204':'3Days', '1207':'6Days', '1211':'10Days', '1215':'14Days' }
    print 'Deadline on this inquiry ' + deadline_dict[deadline]