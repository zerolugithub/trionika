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
    print 'Create order on PW'
    s('#order_now_big_btn_main').click()

def click_inquiry_button():
    print 'Create inquiry on PW'
    s('#main > div:nth-child(1) > div > div:nth-child(3) > div > span.head-text').click()

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s(by.text('Sign in')).click()

def choice_deadline():
    n = random.randint(0, 8)
    deadline_list = ['935', '936', '937', '902', '903','904', '907', '911', '915' ]
    deadline = deadline_list[n]
    s(by.xpath('//input[@name="deadline"][@value="%s"]/..'%deadline)).click()
    deadline_dict = { '935':'3Hours', '936':'6Hours', '937':'12Hours', '902':'24Hours', '903':'2Days','904':'3Days', '907':'6Days', '911':'10Days', '915':'14Days' }
    print 'Deadline on this inquiry ' + deadline_dict[deadline]