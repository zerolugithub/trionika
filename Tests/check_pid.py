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
from Sites.DE import de
from Sites.DW import dw
from Sites.EA import main_page_ea
from Sites.EA import order_ea
from Sites.EDP import main_edp
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

from General_pages import modals, all_site
from General_pages import order_steps
from Sites.DW import dw
from data import topic, paper_details
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

config_browser().chrome_headless()
config.timeout = 10
config.reports_folder = os.path.join(os.getcwd(), "screenshots")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Test_Check_pid:
    driver = browser.driver()

    def setup(m):
        config_browser().chrome_headless()
        print '\n ****************** START TEST CASE ************** \n'

    def teardown(m):
        print '\n ****************** END TEST KEYS ***************** \n'
        browser.driver().delete_all_cookies()
        browser.quit()


# Start test
    @allure.story('Создание заказа и проверка трека статы на PH')
    def test_pid_ph(self):
        browser.open_url("https://www.paperhelp.org/?pid=6402")
        browser.driver().maximize_window()
        ph.proceed_to_order()
        order_steps.i_am_new_for_pid()
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)
        browser.open_url("https://www.edu-profit.com/")
        main_edp.login_ph()
        main_edp.go_to_stata_tab()
        main_edp.check_stata()
    @allure.story('Создание заказа и проверка трека статы на EP')
    def test_pid_ep(self):
        browser.open_url("https://essaypedia.com/?pid=6405")
        browser.driver().maximize_window()
        ep.proceed_to_order()
        order_steps.i_am_new_for_pid()
        order_steps.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        all_site.close_modal_upgrade_now()
        order_steps.checking_price(price)
        browser.open_url("https://www.edu-profit.com/")
        #main_edp.logout()
        main_edp.login_ep()
        main_edp.go_to_stata_tab()
        main_edp.check_stata()
    @allure.story('Создание заказа и проверка трека статы на EW')
    def test_pid_ew(self):
        browser.open_url("https://evolutionwriters.com/?pid=6411")
        browser.driver().maximize_window()
        ew.proceed_to_order()
        order_steps.i_am_new_for_pid()
        order_steps.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        all_site.close_modal_upgrade_now()
        order_steps.checking_price(price)
        browser.open_url("https://www.edu-profit.com/")
        #main_edp.logout()
        main_edp.login_ew()
        main_edp.go_to_stata_tab()
        main_edp.check_stata()
    @allure.story('Создание заказа и проверка трека статы на MAE')
    def test_pid_mae(self):
        browser.open_url("https://myadmissionsessay.com/?pid=6417")
        browser.driver().maximize_window()
        mae.proceed_to_order()
        order_steps.i_am_new_for_pid()
        order_steps.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        all_site.close_modal_upgrade_now()
        order_steps.checking_price(price)
        browser.open_url("https://www.edu-profit.com/")
        #main_edp.logout()
        main_edp.login_mae()
        main_edp.go_to_stata_tab()
        main_edp.check_stata()
    @allure.story('Создание заказа и проверка трека статы на EE')
    def test_pid_ee(self):
        browser.open_url("https://expert-editing.org/?pid=6420")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        ee.proceed_to_order()
        order_steps.i_am_new_for_pid()
        order_steps.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        all_site.close_modal_upgrade_now()
        order_steps.checking_price(price)
        browser.open_url("https://www.edu-profit.com/")
        #main_edp.logout()
        main_edp.login_ee()
        main_edp.go_to_stata_tab()
        main_edp.check_stata()
    @allure.story('Создание заказа и проверка трека статы на PDN')
    def test_pid_pdn(self):
        browser.open_url("https://www.paperduenow.com?pid=6414")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        pdn.proceed_to_order()
        order_steps.i_am_new_for_pid()
        order_steps.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        all_site.close_modal_upgrade_now()
        order_steps.checking_price(price)
        browser.open_url("https://www.edu-profit.com/")
        #main_edp.logout()
        main_edp.login_pdn()
        main_edp.go_to_stata_tab()
        main_edp.check_stata()
    @allure.story('Создание заказа и проверка трека статы на DW')
    def test_pid_dw(self):
        browser.open_url("https://www.dissertationwritings.com?pid=6432")
        browser.driver().maximize_window()
        dw.proceed_to_order()
        order_steps.i_am_new_for_pid()
        dw.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        modals.modal_upgrade_order()
        order_steps.checking_price(price)
        browser.open_url("https://www.edu-profit.com/")
        #main_edp.logout()
        main_edp.login_dw()
        main_edp.go_to_stata_tab()
        main_edp.check_stata()