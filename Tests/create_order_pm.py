#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf8
#import time
#from selene import driver
import os

from EST import order_est
from PM import order_pm
from selene.api import *
from selene.browsers import BrowserName

from General_pages import order_steps
from Sites.PM import main_page_pm
from data import mail, pwd, topic, paper_details, additional_materials_list

config.browser_name = BrowserName.PHANTOMJS
config.hold_browser_open = True
config.timeout = 10
config.desired_capabilities={}
config.reports_folder = os.path.join(os.getcwd(), "screenshots")

class Test_Create_Inquiry_PM:
    driver = browser.driver()

    def setup_module(m):
        config.browser_name = BrowserName.PHANTOMJS
        browser.driver().delete_all_cookies()
    def teatdown(self):
        browser.close()

    def test_Create_Inquiry_PM_Old_Client_Essay_HH_Dissertation(self):  # ---->Chooses the category type of paper: Essay or Homework Help or Dissertation
        browser.open_url("https://papersmaster.com/")
        browser.driver().maximize_window()
        main_page_pm.proceed_to_order()
        order_pm.choice_academic_level()
        order_pm.choice_type_of_paper_essays()
        order_pm.choice_subject_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_pm.login_on_order_page(mail, pwd)
        order_pm.set_number_of_slides()
        order_pm.choice_additional_materials(additional_materials_list)
        order_pm.choice_paper_format_random_step_inquiry()
        order_pm.choice_deadline()
        order_pm.set_number_of_pages()
        order_pm.choice_payment_system()
        price = order_est.order_price()
        order_pm.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    def test_Create_Inquiry_PM_New_Client_Essay_HH_Dissertation(self):  # ---->Chooses the category type of paper: Essay or Homework Help or Dissertation
        browser.open_url("https://papersmaster.com/")
        browser.driver().maximize_window()
        main_page_pm.proceed_to_order()
        order_pm.choice_academic_level()
        order_pm.choice_type_of_paper_essays()
        order_pm.choice_subject_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_pm.regigister()
        order_pm.set_number_of_slides()
        order_pm.choice_additional_materials(additional_materials_list)
        order_pm.choice_paper_format_random_step_inquiry()
        order_pm.choice_deadline()
        order_pm.set_number_of_pages()
        order_pm.choice_payment_system()
        price = order_est.order_price()
        order_pm.click_proceed_to_secure_payment()
        order_steps.checking_price(price)
        browser.close()




