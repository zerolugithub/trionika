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
    print 'Create order on UE'
    s('.order-btn').click()


@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s(by.xpath('.//*[@id="header"]/nav/div[1]/div/div/div/div[2]/button')).click()


@allure.step("Вводим мейл и пароль, нажимаем кнопку Submit ")
def set_mail_and_pass(mail, pwd):
    time.sleep(1)
    s('#loginEmail').set_value(mail)
    time.sleep(1)
    s('#loginPass').set_value(pwd)
    s('.order-btn.admin-auth').click()

@allure.step('Заполнение формы для регистрации нового пользователя')
def i_am_new():
    s(by.xpath('//li[@tab-target="_create_client"]/a')).click()
    s('#no_match_email > input').set_value(random_mail())
    s('[name="first_name"]').set_value('Test')
    s('[name="last_name"]').set_value('test')
    s('[name="phone_number"]').set_value('123123123')
    time.sleep(1)
    s('#butt_next_2').click()