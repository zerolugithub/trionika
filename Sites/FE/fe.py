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
    print 'Create order on FE'
    browser.driver().execute_script(("window.scrollTo(0, document.body.scrollHeight);"))
    s(by.xpath('//a[@class="pay-btn"]')).click()

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s(by.text('Sign in')).click()

@allure.step("Вводим мейл и пароль, нажимаем кнопку Submit ")
def set_mail_and_pass(mail, pwd):
    s('[name="email"]').set_value(mail)
    time.sleep(2)
    s('[name="pass"]').set_value(pwd)
    time.sleep(2)
    s(by.xpath('.//*[@id="auth-form"]/div[2]/button[1]')).click()

def i_am_new():
    s(by.xpath('//li[@tab-target="_create_client"]/a')).click()
    time.sleep(1)
    url = browser.driver().current_url
    if 'order2' in url:                                                   # For A/B testing
        print 'A/B test for field Name'
        s(by.xpath('.//*[@id="no_match_email"]/input')).set_value(random_mail())
        s('[name="name_user_b"]').set_value('Test Test')
        s('[name="phone_number"]').set_value('123123123')
    else:
        s(by.xpath('.//*[@id="no_match_email"]/input')).set_value(random_mail())
        s('[name="first_name"]').set_value('Test')
        s('[name="last_name"]').set_value('test')
        s('[name="phone_number"]').set_value('123123123')
    time.sleep(1)
    s('#butt_next_2').click()

@allure.step('Нажимаем на главной странице кнопку Inquiry')
def click_inquiry_button():
    print 'Create inquiry on FE'
    s('a[href="/inquiry.html"]').click()

@allure.step('Заполнение формы для регистрации нового пользователя')
def i_am_new_inquiry():
    s('#order_contact_block > ul > li:nth-child(2) > a').click()
    s('[name="first_name"]').set_value('Test')
    s('[name="last_name"]').set_value('test')
    s(by.xpath('.//*[@id="no_match_email"]/input')).set_value(random_mail())
    s('[name="phone_number"]').set_value('123123123')

# def click_inquiry_button():
#     s('a[href="/inquiry.html"]').click()

def click_submit_inquiry_button():
    browser.driver().execute_script(("window.scrollTo(0, document.body.scrollHeight);"))
    time.sleep(1)
    s(by.xpath('//button[@class="button button-primary btn-large btn-procced wait-go"]')).click()
    time.sleep(8)

def change_inquiry_to_order():
    time.sleep(2)
    price = s(by.xpath('//tr[@class="main-list-item unpaid-order inquiry_processing-status"][1]/td[@class="price"]')).text
    price = price[1:]
    s(by.xpath('//tr[@class="main-list-item unpaid-order inquiry_processing-status"][1]/td[@class="action"]/a')).click()
    return price

def click_discount_button_on_header():
    s(by.xpath('//a[@class="btn-default pull-right"]')).click()

def choice_deadline():
    n = random.randint(0, 8)
    deadline_list = ['735', '736', '737', '702', '703','704', '707', '711', '715' ]
    deadline = deadline_list[n]
    s(by.xpath('//input[@name="deadline"][@value="%s"]/..'%deadline)).click()
    deadline_dict = { '735':'3Hours', '736':'6Hours', '737':'12Hours', '702':'24Hours', '703':'2Days','704':'3Days', '707':'6Days', '711':'10Days', '715':'14Days' }
    print 'Deadline on this inquiry ' + deadline_dict[deadline]