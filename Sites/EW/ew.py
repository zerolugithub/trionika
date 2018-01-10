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

from selenium.common.exceptions import TimeoutException

from General_pages.order_steps import random_mail


@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s(by.xpath('//a[@class="sign-in"]')).click()

@allure.step('Нажимаем на главной странице кнопку Order')
def proceed_to_order():
    print 'Create order on EW'
    s('.btn.btn-primary').click()

def go_to_admin_after_order():
    browser.open_url("https://evolutionwriters.com/")
    s('.btn-sign-in').click()

@allure.step('Нажимаем на главной странице кнопку Inquiry')
def click_inquiry_button():
    print 'Create inquiry on EW'
    #s(by.text('Free Inquiry')).click()
    s('#navbar > ul > li:nth-child(5) > a').click()


def change_inquiry_to_order():
    time.sleep(2)
    price = s(by.xpath('//tr[@class="main-list-item unpaid-order inquiry_processing-status"][1]/td[@class="price"]')).text
    price = price[1:]
    s(by.xpath('//tr[@class="main-list-item unpaid-order inquiry_processing-status"][1]/td[@class="action"]/a')).click()
    return price

@allure.step('Устанавливаем рандомный Deadline')
def choice_deadline():
    n = random.randint(0, 8)
    deadline_list = ['435', '436', '437', '402', '403','404', '407', '411', '415' ]
    deadline = deadline_list[n]
    s(by.xpath('//input[@name="deadline"][@value="%s"]/..'%deadline)).click()
    deadline_dict = { '435':'3Hours', '436':'6Hours', '437':'12Hours', '402':'24Hours', '403':'2Days','404':'3Days', '407':'6Days', '411':'10Days', '415':'14Days' }
    print 'Deadline on this inquiry ' + deadline_dict[deadline]

@allure.step('Генерируем случайное число и вводим в поле Number of Pages')
def set_number_of_pages_random():
    time.sleep(2)
    n = random.randint(1, 15)
    s('[name="pages"]').set_value(n).press_enter()
    n = str(n)
    print 'Count of pages is ' + n
    while True:
        try:
            alert = s(by.xpath('//div[@error="pages"]')).text
        except TimeoutException:
            return True
        else:
            alert = s(by.xpath('//div[@error="pages"]')).text
            print alert
            if len(alert)==71 or len(alert)==69:
                count = alert.split(' ')[-9]
                s('[name="pages"]').set_value(count)
                print 'Count of pages change to ' + count + ' because deadline it does not allow more'
            elif len(alert)==83:
                count = alert.split(' ')[-10]
                s('[name="pages"]').set_value(count)
                print 'Count of pages change to ' + count + ' because deadline it does not allow more'
            else:
                "Input pages has error !!! "
                break
