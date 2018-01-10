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

@allure.step('Выбираем случайны  Subject')
def choice_subject_random():
    n = str(random.randint(2, 20))
    #time.sleep(1)
    #s(by.xpath('.//*[@id="select2"]')).click()
    time.sleep(1)
    s(by.xpath('.//*[@id="select2"]/optgroup/option[' + n + ']')).click()
    #s('#topic').click()

@allure.step('Заполняем поле Topic - Test')
def set_topic(topic):
    s('#topic').set_value(topic)

@allure.step('Заполняем поле Paper Details: - IT Test Autamation ')
def set_paper_details(paper_details):
    s('#instructions').set_value(paper_details)

@allure.step('Выбираем  Paper Format')
def choice_paper_format():
    n = str(random.randint(2, 5))
    s(by.xpath('//select[@id="select4"]/option[' + n + ']')).click()

@allure.step(' Нажать на кнопку "Proceed to payment"')
def click_proceed_to_secure_payment():
    s('#create_order').click()

@allure.step('Генерируем случайное число и вводим в поле Number of slides')
def set_number_of_slides():
    n = random.randint(1, 10)
    s('._slides.form-input').set_value(n)

@allure.step('Регистрация на сайте нового пользователя')
def regigister():
    time.sleep(1)
    s('#ui-id-1').click()
    s('#name').set_value('Test')
    s('#surname').set_value('test')
    s('#email1').set_value(random_mail())
    s('#password1').set_value('123123')
    s('[name="phone_number"]').set_value('123123123')

@allure.step('Заполнение формы для регистрации старого пользователя')
def login_on_order_page(email, pwd):
    time.sleep(1)
    s('#ui-id-2').click()
    s('#email').set_value(email)
    s('#password').set_value(pwd)

@allure.step('Запоминаем значение поля TOTAL PRICE')
def order_price():
    time.sleep(2)
    price = s('#appr_price').text
    price = price[1:]
    print "Price on this order " + price + '$'
    return price
