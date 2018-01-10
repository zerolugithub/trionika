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

@allure.step('Нажимаем на главной странице кнопку Order Now!')
def proceed_to_order():
    print 'Create order on EST'
    s(by.text('Order Now!')).click()

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s(by.xpath('//a[@class="btn btn-inverse-blue"]')).click()

