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
from data import discount_error, discount, paypalLogin, paypalPass, mail, pwd
from selenium import webdriver
from General_pages.order_steps import random_mail


@allure.step('Нажать на кнопку Login')
def login():
    print 'Create order on EA'
    s('#inputEmail').set_value(mail)
    s('#inputPassword').set_value(pwd)
    s(by.text('Login')).click()

@allure.step('Нажать на кнопку Sign Up')
def sign_up():
    print 'Create order on EA'
    s(by.text('Sign Up')).click()
    s('[name="first_name"]').set_value('Test')
    s('[name="last_name"]').set_value('test')
    s('[name="email"]').set_value(random_mail())
    s('[name="phone_number"]').set_value('123123123')

@allure.step('Нажать на кнопку Registrarion для нового пользователя')
def click_register_button():
    s(by.xpath('//button[@class="btn btn-primary"]')).click()
    time.sleep(3)

@allure.step('Выход из учетной записи на сайте EA')
def sign_out():
    if s(by.xpath('//a[@class="user-sign-out"]')).is_displayed():
        s(by.xpath('//a[@class="user-sign-out"]')).click()



