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
    print 'Create order on AP'
    s('body > main > div.action-block > div > aside > div.the-right-way-content > div > div > a').click()

@allure.step('Выбираем случайны  Subject')
def choice_subject_random():
    n = str(random.randint(2, 69))
    time.sleep(1)
    s(by.xpath('//div/input[@id="subject_autocomplete"]')).click()
    s(by.xpath('//ul[@id="ui-id-1"]/li[' + n + ']')).click()

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s(by.xpath('/html/body/main/div[3]/div/aside/a[1]')).click()