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
    print 'Create order on MAE'
    s(by.text('order now')).click()
    # wrapper > div.front-hero > div > div > div.table-cell.calc-holder > div > form > div > a

def click_inquiry_button():
    print 'Create inquiry on MAE'
    s(by.text('Free Inquiry')).click()

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s(by.text('sign in')).click()

def choice_deadline():
    n = random.randint(0, 8)
    deadline_list = ['1135', '1136', '1137', '1102', '1103','1104', '1107', '1111', '1115' ]
    deadline = deadline_list[n]
    s(by.xpath('//input[@name="deadline"][@value="%s"]/..'%deadline)).click()
    deadline_dict = { '1135':'3Hours', '1136':'6Hours', '1137':'12Hours', '1102':'24Hours', '1103':'2Days','1104':'3Days', '1107':'6Days', '1111':'10Days', '1115':'14Days' }
    print 'Deadline on this inquiry ' + deadline_dict[deadline]