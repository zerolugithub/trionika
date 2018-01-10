# coding: utf8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string
import allure
import pytest
import selene
from selene.conditions import text
from selene.api import *
import time

from General_pages.order_steps import random_mail

@allure.step('Нажимаем на главной странице кнопку Order')
def proceed_to_order():
    print 'Create order on PDN'
    #time.sleep(3)
    url = browser.driver().current_url
    if "/home2" in url:
        s(".order-link-header").click()
    else:
        s(".order-btn.order-non-mob.order-button-ga").click()
    #s(by.xpath('//a[@href="/order.html"]')).click()

def click_inquiry_button():
    print 'Create inquiry on PDN'
    s(by.text('Free Inquiry')).click()

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    time.sleep(3)
    url = browser.driver().current_url
    if "/home2" in url:
        s(by.xpath('//*[@id="navbar"]/ul/li[8]/a')).click()
    else:
        s(by.xpath('//*[@id="main-page"]/header/div/div/div[2]/a[2]/span')).click()

def choice_deadline():
    n = random.randint(0, 8)
    deadline_list = ['1435', '1436', '1437', '1402', '1403','1404', '1407', '1411', '1415' ]
    deadline = deadline_list[n]
    s(by.xpath('//input[@name="deadline"][@value="%s"]/..'%deadline)).click()
    deadline_dict = { '1435':'3Hours', '1436':'6Hours', '1437':'12Hours', '1402':'24Hours', '1403':'2Days','1404':'3Days', '1407':'6Days', '1411':'10Days', '1415':'14Days' }
    print 'Deadline on this inquiry ' + deadline_dict[deadline]