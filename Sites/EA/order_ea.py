# coding: utf8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string
import allure
import pytest
import requests
import selene
from selene import driver
from selene import tools
from selene.conditions import text, visible
from selene.api import *
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from data import discount_error, discount, paypalLogin, paypalPass
from selenium import webdriver


from General_pages.order_steps import random_mail

@allure.step('Нажать на кнопку "New order" в админке клиента на сайте EA')
def new_order():
    time.sleep(1)
    s(by.xpath('//a[@href="/order"][2]')).click()


@allure.step('Выбираем случайны  Subject')
def choice_subject_random():
    n = str(random.randint(2, 69))
    time.sleep(1)
    s('#subject_test').click()
    s(by.xpath('//ul[@id="ui-id-1"]/li[' + n + ']')).click()

@allure.step('нажать на кнопку "Proceed to Secure Payment"')
def click_Proceed_to_Secure_Payment():
    s('.btn.btn-primary.btn-large.wait-go').click()

@allure.step('Запоминаем значение поля TOTAL PRICE')
def order_price():
    time.sleep(2)
    price = s('.price_strong.strong_price_order').text
    price = price[1:]
    return price