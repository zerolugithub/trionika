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
    s(by.xpath('//a[@class="sign-link-new"]')).click()

@allure.step('Нажимаем на главной странице кнопку Order')
def proceed_to_order():
    s(by.text('Sign in')).click()

@allure.step('Нажимаем на главной странице кнопку Order')
def proceed_to_order():
    print 'Create order on WMP'
    s(by.xpath('//a[@href="/order.html"]/span')).click()

@allure.step('Выбираем случайны  Subject')
def choice_subject_random():
    n = str(random.randint(2, 13))
    time.sleep(2)
    s('#subject_test').click()
    time.sleep(2)
    s(by.xpath('//ul[@id="ui-id-1"]/li[' + n + ']')).click()

@allure.step('Нажимаем на главной странице кнопку Inquiry')
def click_inquiry_button():
    print 'Create inquiry on WMP'
    s('a[href="/inquiry.html"]').click()

@allure.step('Нажимаем на кнопку "Submit order" в админке клиента')
def click_submit_inquiry_button():
    browser.driver().execute_script(("window.scrollTo(0, document.body.scrollHeight);"))
    s(by.xpath('//button[@class="button button-primary btn-large btn-procced wait-go"]')).click()

@allure.step('Нажимаем на кнопку "Submit order" в админке клиента')
def change_inquiry_to_order():
    time.sleep(10)
    order_number = s(by.xpath('.//tbody/tr/td[1]/span')).text
    #price = s(by.xpath('//tr[@class="main-list-item unpaid-order inquiry_processing-status"][1]/td[@class="price"]')).text
    price = s(by.xpath('.//tbody/tr/td[5]')).text
    price = price[1:]
    #s(by.xpath('//tr[@class="main-list-item unpaid-order inquiry_processing-status"][1]/td[@class="action"]/a')).click()
    s(by.xpath('.//tbody/tr/td[9]/a[contains(text(),"Submit order")]')).click()
    print 'Current order is ' + order_number + ' and price ' + price + '$'
    return price

@allure.step('Заполнение формы для регистрации нового пользователя')
def i_am_new_inquiry():
    #s('#order_contact_block > ul > li:nth-child(2) > a').click()
    s('[name="first_name"]').set_value('Test')
    s('[name="last_name"]').set_value('test')
    s('[name="email"]').set_value(random_mail())
    s('[name="phone_number"]').set_value('123123123')

@allure.step('Заполнение формы для регистрации старого пользователя')
def sign_in_inquiry(email, pwd):
    s(by.text('Returning client')).click()
    s('[name="email_reg"]').set_value(email)
    s('[name="password_reg"]').set_value(pwd)

def click_discount_button_on_header():
    s('.discount-code').click()

@allure.step('Устанавливаем рандомный Deadline')
def choice_deadline():
    n = random.randint(0, 8)
    deadline_list = ['635', '636', '637', '602', '603','604', '607', '611', '615' ]
    deadline = deadline_list[n]
    s(by.xpath('//input[@name="deadline"][@value="%s"]/..'%deadline)).click()
    deadline_dict = { '635':'3Hours', '636':'6Hours', '637':'12Hours', '602':'24Hours', '603':'2Days','604':'3Days', '607':'6Days', '611':'10Days', '615':'14Days' }
    print 'Deadline on this inquiry ' + deadline_dict[deadline]

# Type of paper  - Questions
@allure.step('Случайный выбор Type of paper  - Questions')
def choice_type_of_paper_Questions():
    type_of_paper = s(by.xpath('.//*[@id="type_of_paper"]/optgroup[2]/option[30]')).text
    s(by.xpath('.//*[@id="type_of_paper"]/optgroup[2]/option[30]')).click()
    print 'Type of paper is ' + type_of_paper

# Type of paper  - Problems
@allure.step('Случайный выбор Type of paper  - Problems')
def choice_type_of_paper_Problems():
    type_of_paper = s(by.xpath('.//*[@id="type_of_paper"]/optgroup[2]/option[35]')).text
    s(by.xpath('.//*[@id="type_of_paper"]/optgroup[2]/option[35]')).click()
    print 'Type of paper is ' + type_of_paper