#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf8
import os

import allure
from selene.api import *
from selene.browsers import BrowserName

from General_pages import modals, all_site
from General_pages import order_steps
from Sites.AP import ap
from Sites.CW import cw
from Sites.DE import de
from Sites.DW import dw
from Sites.EA import main_page_ea
from Sites.EA import order_ea
from Sites.EE import ee
from Sites.EP import ep
from Sites.EST import main_page_est
from Sites.EST import order_est
from Sites.ET import main_page_et
from Sites.ET import order_et
from Sites.EW import ew
from Sites.FE import fe
from Sites.FH import fh
from Sites.LME import lme
from Sites.MAE import mae
from Sites.PDN import pdn
from Sites.PH import ph
from Sites.PM import main_page_pm
from Sites.PM import order_pm
from Sites.PW import pw
from Sites.UE import ue
from Sites.WMP import wmp
from Sites.ws import ws
from data import mail, pwd, topic, paper_details, subject_list
from tools import phantom_js_clean_up, config_browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

config_browser().chrome_headless()
config.timeout = 10
config.reports_folder = os.path.join(os.getcwd(), "screenshots")


class Test_Create_order_steps:
    driver = browser.driver()

    def setup(m):
        config_browser().chrome_headless()
        browser.driver().delete_all_cookies()
        print '\n ****************** START TEST CASE ************** \n'

    def teardown(m):
        print '\n ****************** END TEST KEYS ***************** \n'
        browser.close()

    # _________________________________________________DE________________________________
    @allure.feature('Case 1 ')
    @allure.story('First test')
    def test_1(self):
        print 'First test'

    @allure.feature('Case 1 ')
    @allure.story('Title PH')
    def test_2(self):
        browser.open_url("https://www.paperhelp.org/")
        print browser.driver().title

    @allure.feature('Case 2 ')
    @allure.story('Second test')
    def test_3(self):
        print 'Second test'

    @allure.feature('Case 2 ')
    @allure.story('Title PH 2')
    def test_4(self):
        browser.open_url("https://www.paperhelp.org/")
        print browser.driver().title
