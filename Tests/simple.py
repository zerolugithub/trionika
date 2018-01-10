#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf8
import os

import allure
from selene.api import *
from selene.browsers import BrowserName

from General_pages import modals
from General_pages import order_steps, all_site, order_admin
from Sites.DE import de
from Sites.DW import dw
from Sites.EP import ep
from Sites.ET import main_page_et
from Sites.ET import order_et
from Sites.EW import ew
from Sites.FE import fe
from Sites.FH import fh
from Sites.LME import lme
from Sites.MAE import mae
from Sites.PDN import pdn
from Sites.PH import ph
from Sites.PW import pw
from Sites.WMP import wmp
from data import mail, pwd, topic, paper_details, subject_list, additional_materials_list
from tools import phantom_js_clean_up
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(executable_path='/Users/user/Desktop/chromedriver',chrome_options=chrome_options)
browser.set_driver(driver)
config.browser_name = BrowserName.CHROME
config.timeout = 10
config.reports_folder = os.path.join(os.getcwd(), "screenshots")


class Test_Create_order_steps:
    driver = browser.driver()

    def setup(m):
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument("--window-size=1920,1080")
        # driver = webdriver.Chrome(executable_path='/Users/user/Desktop/chromedriver', chrome_options=chrome_options)
        # browser.set_driver(driver)
        # config.browser_name = BrowserName.CHROME
        print '\n ****************** START TEST CASE ************** \n'

    def teardown(m):
        print '\n ****************** END TEST KEYS ***************** \n'
        browser.driver().delete_all_cookies()

    # _________________________________________________DE________________________________
    @allure.feature('Создание заказа через админку клиента FH')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_fh2(self):
        browser.open_url("http://www.freelancehouse.co.uk/")
        browser.driver().maximize_window()
        fh.click_sign_in()
        order_admin.set_mail_and_pass(mail, pwd)
        order_admin.click_create_order_button_admin()
        order_admin.choice_type_of_paper_essays()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details_LI()
        order_admin.set_number_of_slides()
        order_admin.choice_paper_format_random_step_inquiry()
        order_admin.set_number_of_sources()
        order_admin.choice_additional_materials(additional_materials_list)
        order_admin.choice_Plagiarism_report()
        order_admin.choice_Abstract_page()
        order_admin.choice_VIP_customer_sevice()
        order_admin.choice_payment_system()
        price = order_steps.submit_proceed_to_secure_payment()
        modals.modal_upgrade_order()
        order_steps.checking_price(price)
        #browser.driver().close()
        browser.driver().quit()

