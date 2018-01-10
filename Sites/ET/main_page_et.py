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


@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    time.sleep(1)
    s('#navigation > div.secondMenu > ul > li.menu-1240 > a').click()   # //*[@id="navigation"]/div[3]/ul/li[4]/a

@allure.step('Нажимаем на главной странице кнопку Order')
def proceed_to_order():
    print 'Create order on ET'
    s(by.xpath('//input[@value="Proceed"]')).click()

@allure.step('Заполнение формы для регистрации нового пользователя')
def i_am_new():
    time.sleep(1)
    s(by.xpath('//li[@tab-target="_create_client"]/a')).click()
    s('[name="first_name"]').set_value('Test')
    s('[name="last_name"]').set_value('test')
    s('[name="email"]').set_value(random_mail())
    s('[name="phone_number"]').set_value('123123123')
    s('[name="phone_area"]').set_value('123')
    time.sleep(1)
    s(by.xpath('.//*[@id="butt_next_2"][contains(text(),"Proceed")]')).click()

@allure.step('Заполнение формы для регистрации старого пользователя')
def sign_in(email, pwd):
    time.sleep(1)
    s(by.xpath('//li[@tab-target="_client_login"]/a')).click()
    s('[name="email_reg"]').set_value(email)
    s('[name="password_reg"]').set_value(pwd)
    s(by.xpath('.//*[@id="butt_next_2"][contains(text(),"Login")]')).click()

@allure.step('Выбираем случайны  Subject')
def choice_subject_random():
    n = str(random.randint(2, 30))
    time.sleep(1)
    s(by.xpath('.//*[@id="select_subject"]')).click()
    s(by.xpath('//li[@class="ui-menu-item"][' + n + ']')).click()

@allure.step('Нажимаем на главной странице кнопку Inquiry')
def click_inquiry_button():
    print 'Create inquiry on ET'
    time.sleep(2)
    s(by.xpath('.//*[@id="block-block-30"]/div[2]/a[2]')).click()

@allure.step('Нажимаем на главной странице кнопку Submit Inquiry')
def click_submit_inquiry_button():
    time.sleep(2)
    s(by.xpath('.//*[@id="order-step-1"]/div[18]/div/button')).click()
    time.sleep(10)

@allure.step('Нажимаем на главной странице кнопку Discount')
def click_discount_button_on_header():
    s('.discount-code').click()
