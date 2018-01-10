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


def proceed_to_order():
    print 'Create order on PM'
    s(by.text('Order now')).click()

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s(by.xpath('/html/body/header/div[1]/div/div/div[2]/a[6]')).click()