# coding: utf8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string

import datetime

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
from data import discount_error, discount, paypalLogin, paypalPass, mail, pwd, log_edp_ph, pass_edp, log_edp_ep, \
    log_edp_ew, log_edp_pdn, log_edp_mae, log_edp_ee, log_edp_dw
from selenium import webdriver
from General_pages.order_steps import random_mail
from tools import scrollDown

dt = datetime.datetime.now()
dt =dt.strftime("%m/%d/%Y")
dt=str(dt)

@allure.step('Выход из учетной записи')
def logout():
    s(by.xpath('//div[@class="hello"]/span')).click()
    time.sleep(2)
    s(by.xpath('//a[@class="logout"]')).click()
    time.sleep(4)

@allure.step('Вход в учетную запись с параметрами')
def login_edp(login,pwd):
    s(by.xpath('//a[@href="/login.html"]')).click()
    s('#login_login').set_value(login)
    s('#login_password').set_value(pwd)
    s('.login').click()

@allure.step('Вход в учетную записи для сайта PH')
def login_ph():
    s(by.xpath('//a[@href="/login.html"]')).click()
    s('#login_login').set_value(log_edp_ph)
    s('#login_password').set_value(pass_edp)
    s('.login').click()

@allure.step('Вход в учетную записи для сайта EP')
def login_ep():
    s(by.xpath('//a[@href="/login.html"]')).click()
    s('#login_login').set_value(log_edp_ep)
    s('#login_password').set_value(pass_edp)
    s('.login').click()

@allure.step('Вход в учетную записи для сайта EW')
def login_ew():
    s(by.xpath('//a[@href="/login.html"]')).click()
    s('#login_login').set_value(log_edp_ew)
    s('#login_password').set_value(pass_edp)
    s('.login').click()

@allure.step('Вход в учетную записи для сайта PDN')
def login_pdn():
    s(by.xpath('//a[@href="/login.html"]')).click()
    s('#login_login').set_value(log_edp_pdn)
    s('#login_password').set_value(pass_edp)
    s('.login').click()

@allure.step('Вход в учетную записи для сайта DW')
def login_dw():
    s(by.xpath('//a[@href="/login.html"]')).click()
    s('#login_login').set_value(log_edp_dw)
    s('#login_password').set_value(pass_edp)
    s('.login').click()

@allure.step('Вход в учетную записи для сайта MAE')
def login_mae():
    s(by.xpath('//a[@href="/login.html"]')).click()
    s('#login_login').set_value(log_edp_mae)
    s('#login_password').set_value(pass_edp)
    s('.login').click()

@allure.step('Вход в учетную записи для сайта EE')
def login_ee():
    s(by.xpath('//a[@href="/login.html"]')).click()
    s('#login_login').set_value(log_edp_ee)
    s('#login_password').set_value(pass_edp)
    s('.login').click()

@allure.step('Переход во вкладку "Стата"')
def go_to_stata_tab():
    s(by.xpath('.//*[@id="header"]/div[2]/div/ul/li[1]/a')).click()

@allure.step('Проверка показателя статы на текущий день')
def check_stata():
    time.sleep(5)
    scrollDown()
    dt = datetime.datetime.now()
    dt = dt.strftime("%m/%d/%Y")
    dt = str(dt)
    print 'Current date is ' + dt
    unik_field = s(by.xpath('//div[@class="table-stats-resp-con stats-block"]/div[2]/table[1]/tbody/tr/td[contains(text(), "{0}")]/../td[2]'.format(dt))).text
    if unik_field == '2':
        print 'Count unik ' +  unik_field + " in " + dt
    else:
        print 'Error unik test ! Unik = ' + unik_field
        s('. Error for unik').click()
    bid_field = s(by.xpath('//div[@class="table-stats-resp-con stats-block"]/div[2]/table[1]/tbody/tr/td[contains(text(), "{0}")]/../td[3]'.format(dt))).text
    if bid_field == '0':
        print 'Count bid ' +  bid_field + " in " + dt
    else:
        print 'Error bid test ! Bid = ' + bid_field
        s('. Error for unik').click()
    #bid =  s(by.xpath('//div[@class="table-stats-resp-con stats-block"]/div[2]/table[1]/tbody/tr/td[contains(text(), "{0}")]/../td[3]'.format(dt))).text().assure('0')