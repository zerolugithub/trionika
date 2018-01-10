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


@allure.step('Выбираем случайны  Paper Format')
def choice_paper_format():
    s(by.xpath('//select[@class="form-element custom-select order-desktop-view"]')).click()
    s(by.xpath('//select[@class="form-element custom-select order-desktop-view"]/option[2]')).click()

@allure.step(' Нажать на кнопку "Proceed to payment"')
def click_proceed_to_secure_payment():
    s('.btn-procced.wait-go.button-next-step.wait-go').click()

@allure.step('Случайный выбор Subject')
def choice_subject_random(subject_list):
    n = str(random.randint(2, 69))
    time.sleep(1)
    s(by.xpath('//select[@name="subject"]')).click()
    s(by.xpath('//select[@name="subject"]/option[' + n + ']')).click()
    n = int(n)
    subject = subject_list[n]
    print 'Order subject is ' + subject

@allure.step('Устанавливаем рандомный Deadline')
def choice_deadline():
    n = random.randint(0, 8)
    deadline_list = ['1735', '1736', '1737', '1702', '1703','1704', '1707', '1711', '1715' ]
    deadline = deadline_list[n]
    s(by.xpath('//input[@name="deadline"][@value="%s"]/..'%deadline)).click()
    deadline_dict = { '1735':'3Hours', '1736':'6Hours', '1737':'12Hours', '1702':'24Hours', '1703':'2Days','1704':'3Days', '1707':'6Days', '1711':'10Days', '1715':'14Days' }
    print 'Deadline on this inquiry ' + deadline_dict[deadline]