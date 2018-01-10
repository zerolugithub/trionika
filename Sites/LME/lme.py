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
    print 'Create order on LME'
    s('.continue').click()

@allure.step('Выбираем случайны  Subject')
def choice_subject_random():
    n = str(random.randint(2, 69))
    time.sleep(1)
    s('#subject_test').click()
    s(by.xpath('//ul[@id="ui-id-1"]/li[' + n + ']')).click()

def click_inquiry_button():
    print 'Create inquiry on LME'
    s(by.text('Inquiry')).click()

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s('body > header > nav > div.top > div > div > div > div > a.login').click()

def choice_deadline():
    n = random.randint(0, 8)
    deadline_list = ['4135', '4136', '4137', '4102', '4103','4104', '4107', '4111', '4115' ]
    deadline = deadline_list[n]
    s(by.xpath('//input[@name="deadline"][@value="%s"]/..'%deadline)).click()
    deadline_dict = { '4135':'3Hours', '4136':'6Hours', '4137':'12Hours', '4102':'24Hours', '4103':'2Days','4104':'3Days', '4107':'6Days', '4111':'10Days', '4115':'14Days' }
    print 'Deadline on this inquiry ' + deadline_dict[deadline]