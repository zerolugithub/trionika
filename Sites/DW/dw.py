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
    print 'Create order on DW'
    s('.order_check').click()

@allure.step('Нажимаем на главной странице кнопку Inquiry')
def click_inquiry_button():
    print 'Create inquiry on DE'
    s(by.xpath('/html/body/div[10]/div[1]/div/a')).click()

@allure.step('Нажимаем на главной странице кнопку Discount')
def click_discount_button_on_header():
    s(by.xpath('//button[@class="btn"]')).click()

@allure.step('Случайный выбор Subject')
def choice_subject_random():
    n = str(random.randint(2, 50))
    time.sleep(1)
    s('#subject_autocomplete').click()
    s(by.xpath('//ul[@id="ui-id-1"]/li[' + n + ']')).click()

@allure.step('Устанавливаем рандомный Deadline')
def choice_deadline():
    n = random.randint(0, 8)
    deadline_dict = {'835': '3Hours', '836': '6Hours', '837': '12Hours', '802': '24Hours', '803': '2Days',
                     '804': '3Days', '807': '6Days', '811': '10Days', '815': '14Days'}
    deadline_list = ['835', '836', '837', '802', '803','804', '807', '811', '815' ]
    deadline = deadline_list[n]
    if s(by.xpath('//input[@name="deadline"][@value="%s"]/..'%deadline)).is_displayed():
        s(by.xpath('//input[@name="deadline"][@value="%s"]/..'%deadline)).click()
        print 'Deadline on this inquiry ' + deadline_dict[deadline]
    else:
        m = random.randint(1, 7)
        deadline = deadline_list[n]
        s(by.xpath('//input[@name="deadline"][@value="%s"]/..' % deadline)).click()
        deadline_dict = {'803': '2Days', '804': '3Days', '807': '6Days', '811': '10Days', '815': '14Days', '833': '1Months','834': '2Months',}


def choice_type_of_paper_essays():
    a = str(random.randint(1, 3))
    if a == '2':
        print 'Сategory  - Essays'
        count = str(random.randint(1, 24))
    elif a == '1':
        print 'Сategory  - Dissertation'
        print  'Academic level change to Professional'
        count = str(random.randint(1, 10))
    elif a == '3':
        print 'Сategory  - Homework Help'
        count = str(random.randint(1, 8))
    else:
        count = str(random.randint(1, 6))
    type_of_paper = s(by.xpath('.//select[@id="type_of_paper"]/optgroup[' + a + ']/option[' + count + ']')).text
    s(by.xpath('.//select[@id="type_of_paper"]/optgroup[' + a + ']/option[' + count + ']')).click()
    print 'Type of paper is ' + type_of_paper