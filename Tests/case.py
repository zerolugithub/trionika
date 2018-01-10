#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf8
import os
import itertools
import pytest
import time

from allure_commons.types import AttachmentType
from selene.api import *
import selene
import allure
from selene import browser
from selene import config
from selene.browsers import BrowserName
from selene.helpers import env
from selene.tools import s

from tools import phantom_js_clean_up

search_1 = 'Selenium'
search_2 = 'Selene'
config.browser_name = BrowserName.PHANTOMJS
config.hold_browser_open = True
config.desired_capabilities={}
config.timeout = 10
config.reports_folder = os.path.join(os.getcwd(), "screenshots")
# Test

class TestSomeCase:
    driver = browser.driver()

    def setup(m):
        browser.driver().delete_all_cookies()
        print '\n ****************** START TEST CASE ************** \n'

    def teardown(m):
        print '\n ****************** END TEST KEYS ***************** \n'
        browser.quit()

    @classmethod
    def tearDownClass(cls):
        browser.driver().delete_all_cookies()
        """Tear down class."""
        try:
            cls.driver.quit()
            phantom_js_clean_up()
        except Exception as err:
            print(err)

    @pytest.allure.story('Поиск на сайте Google.com')
    def test_step_1(self):
        main_page().open_browser()
        main_page().google_search(search_1)
        main_page().click_search()
        browser.close()

    @pytest.allure.story('КОля? шо по шапкам')
    def test_step_2(self):
        main_page().open_browser()
        main_page().google_search(search_2)
        main_page().click_search()
        browser.close()


    @pytest.allure.story('Поиск на сайте Google.com 1')
    def test_step_3(self):
        main_page().open_browser()
        main_page().google_search(search_1)
        main_page().click_search()
        browser.close()


    @pytest.allure.story('Поиск на сайте Google.com 2')
    def test_step_4(self):
        main_page().open_browser()
        main_page().google_search(search_1)
        main_page().click_search()
        browser.close()

class main_page2:

    def printt(self):
        print "pass"

class main_page():

    @pytest.allure.step(" Переходим на сайт https://www.google.com/ ")
    def open_browser(self):
        browser.open_url('https://www.google.com/')
        browser.driver().maximize_window()
        print "Method # 1"

    @pytest.allure.step("Вводим Trionika в поле поиска ")
    def google_search(self, search):
        s('[name="q"]').send_keys(search).press_enter()
        #s('ss').click()
        print "Method # 1"

    @pytest.allure.step("Нажимаем на кнопку поиска ")
    def click_search(self):
        print "Method # 1"
        print 'Good'