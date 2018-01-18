#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf8
import os

import allure
from selene.api import *
from selene.browsers import BrowserName


from General_pages import order_steps, all_site, order_admin
from Sites.DE import de
from Sites.DW import dw
from Sites.EP import ep
from Sites.ET import main_page_et
from Sites.ET import order_et
from Sites.EW import ew
from Sites.FE import fe
from Sites.LME import lme
from Sites.MAE import mae
from Sites.PDN import pdn
from Sites.PH import ph
from Sites.PW import pw
from Sites.WMP import wmp
from data import mail, pwd, topic, paper_details, subject_list
from tools import phantom_js_clean_up, config_browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

config_browser().chrome_headless()
config.timeout = 10
config.reports_folder = os.path.join(os.getcwd(), "screenshots")


class Test_Create_order_steps:
    #driver = browser.driver()

    def setup(m):
        config_browser().chrome_headless()
        print '\n ****************** START TEST CASE ************** \n'

    def teardown(m):
        print '\n ****************** END TEST KEYS ***************** \n'
        browser.driver().delete_all_cookies()



    @allure.feature('Создание inquiry на PH')
    @allure.story('Создание inquiry - новый пользователь')
    def test_order_ph(self):
        browser.open_url("https://www.paperhelp.org/")
        browser.driver().maximize_window()
        ph.click_inquiry_button()
        order_admin.choice_academic_level()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.choice_deadline()
        order_admin.set_number_of_pages_random()
        order_admin.set_number_of_slides()
        order_admin.i_am_new()
        order_admin.click_submit_inquiry()
        #all_site.close_Authorization_window()
        price = ph.change_inquiry_to_order('new_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    @allure.feature('Создание inquiry на PH')
    @allure.story('Создание inquiry - зарегестрированый пользователь')
    def test_order_ph2(self):
        browser.open_url("https://www.paperhelp.org/")
        browser.driver().maximize_window()
        ph.click_inquiry_button()
        order_admin.choice_academic_level()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.choice_deadline()
        order_admin.set_number_of_pages_random()
        order_admin.set_number_of_slides()
        order_admin.sign_in(mail, pwd)
        order_admin.click_submit_inquiry()
        #all_site.close_Authorization_window()
        price = ph.change_inquiry_to_order('old_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)

    @allure.feature('Создание inquiry на EW')
    @allure.story('Создание inquiry - новый пользователь')
    def test_inquiry_ew(self):
        browser.open_url("https://evolutionwriters.com/")
        browser.driver().maximize_window()
        ew.click_inquiry_button()
        order_admin.choice_academic_level()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.i_am_new()
        order_admin.click_submit_inquiry()
        #all_site.close_Authorization_window()
        price = ph.change_inquiry_to_order('new_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    @allure.feature('Создание inquiry на EW')
    @allure.story('Создание inquiry - зарегестрированый пользователь')
    def test_inquiry_ew2(self):
        browser.open_url("https://evolutionwriters.com/")
        browser.driver().maximize_window()
        ew.click_inquiry_button()
        order_admin.choice_academic_level()
        #order_admin.choice_type_of_paper_essays()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.sign_in(mail, pwd)
        order_admin.click_submit_inquiry()
        #all_site.close_Authorization_window()
        price = ph.change_inquiry_to_order('old_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    @allure.feature('Создание inquiry на WMP')
    @allure.story('Создание inquiry - новый пользователь')
    def test_inquiry_wmp(self):
        browser.open_url("https://www.writemypapers.org/")
        browser.driver().maximize_window()
        wmp.click_inquiry_button()
        order_admin.choice_academic_level()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        wmp.i_am_new_inquiry()
        wmp.click_submit_inquiry_button()
        #all_site.close_Authorization_window()
        price = ph.change_inquiry_to_order('new_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    @allure.feature('Создание inquiry на WMP')
    @allure.story('Создание inquiry - зарегестрированый пользователь')
    def test_inquiry_wmp2(self):
        browser.open_url("https://www.writemypapers.org/")
        browser.driver().maximize_window()
        wmp.click_inquiry_button()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        wmp.sign_in_inquiry(mail, pwd)
        wmp.click_submit_inquiry_button()
        #all_site.close_Authorization_window()
        price = ph.change_inquiry_to_order('old_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    @allure.feature('Создание inquiry на FE')
    @allure.story('Создание inquiry - новый пользователь')
    def test_inquiry_fe(self):
        browser.open_url("https://www.freshessays.com/")
        browser.driver().maximize_window()
        fe.click_inquiry_button()
        order_admin.choice_academic_level()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        fe.i_am_new_inquiry()
        fe.click_submit_inquiry_button()
        #all_site.close_Authorization_window()
        price = ph.change_inquiry_to_order('new_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    @allure.feature('Создание inquiry на FE')
    @allure.story('Создание inquiry - зарегестрированый пользователь')
    def test_inquiry_fe2(self):
        browser.open_url("https://www.freshessays.com/")
        browser.driver().maximize_window()
        fe.click_inquiry_button()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.sign_in(mail, pwd)
        fe.click_submit_inquiry_button()
        #all_site.close_Authorization_window()
        price = ph.change_inquiry_to_order('old_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    @allure.feature('Создание inquiry на PW')
    @allure.story('Создание inquiry - зарегестрированый пользователь')
    def test_order_pw(self):
        browser.open_url("https://www.paperwritings.com/")
        browser.driver().maximize_window()
        pw.click_inquiry_button()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.sign_in(mail, pwd)
        fe.click_submit_inquiry_button()
        #all_site.close_Authorization_window()
        price = ph.change_inquiry_to_order('old_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    @allure.feature('Создание inquiry на PW')
    @allure.story('Создание inquiry - новый пользователь')
    def test_order_pw2(self):
        browser.open_url("https://www.paperwritings.com/")
        browser.driver().maximize_window()
        pw.click_inquiry_button()
        order_admin.choice_academic_level()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.i_am_new()
        fe.click_submit_inquiry_button()
        #all_site.click_done()
        price = ph.change_inquiry_to_order('new_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    # _________________________________________________MAE ________________________________
    @allure.feature('Создание inquiry на MAE')
    @allure.story('Создание inquiry - зарегестрированый пользователь')
    def test_order_mae(self):
        browser.open_url("https://myadmissionsessay.com/")
        browser.driver().maximize_window()
        mae.click_inquiry_button()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.sign_in(mail, pwd)
        fe.click_submit_inquiry_button()
        #all_site.close_Authorization_window()
        price = ph.change_inquiry_to_order('old_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    @allure.feature('Создание inquiry на MAE')
    @allure.story('Создание inquiry - новый пользователь')
    def test_order_mae2(self):
        browser.open_url("https://myadmissionsessay.com/")
        browser.driver().maximize_window()
        mae.click_inquiry_button()
        order_admin.choice_academic_level()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.i_am_new()
        fe.click_submit_inquiry_button()
        #all_site.click_done()
        price = ph.change_inquiry_to_order('new_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    # _________________________________________________EP ________________________________
    @allure.feature('Создание inquiry на EP')
    @allure.story('Создание inquiry - зарегестрированый пользователь')
    def test_order_ep(self):
        browser.open_url("https://essaypedia.com/")
        browser.driver().maximize_window()
        ep.click_inquiry_button()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.sign_in(mail, pwd)
        fe.click_submit_inquiry_button()
        #all_site.close_Authorization_window()
        price = ph.change_inquiry_to_order('old_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    @allure.feature('Создание inquiry на EP')
    @allure.story('Создание inquiry - новый пользователь')
    def test_order_ep2(self):
        browser.open_url("https://essaypedia.com/")
        browser.driver().maximize_window()
        ep.click_inquiry_button()
        order_admin.choice_academic_level()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.i_am_new()
        fe.click_submit_inquiry_button()
        #all_site.click_done()
        price = ph.change_inquiry_to_order('new_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    # _________________________________________________PDN ________________________________
    @allure.feature('Создание inquiry на PDN')
    @allure.story('Создание inquiry - новый пользователь')
    def test_order_pdn(self):
        browser.open_url("https://www.paperduenow.com")
        browser.driver().maximize_window()
        pdn.click_inquiry_button()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.sign_in(mail, pwd)
        fe.click_submit_inquiry_button()
        #all_site.close_Authorization_window()
        price = ph.change_inquiry_to_order('old_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    @allure.feature('Создание inquiry на PDN')
    @allure.story('Создание inquiry - зарегестрированый пользователь')
    def test_order_pdn2(self):
        browser.open_url("https://www.paperduenow.com")
        browser.driver().maximize_window()
        pdn.click_inquiry_button()
        order_admin.choice_academic_level()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.i_am_new()
        fe.click_submit_inquiry_button()
        #all_site.click_done()
        price = ph.change_inquiry_to_order('new_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    # _________________________________________________LME________________________________
    @allure.feature('Создание inquiry на LME')
    @allure.story('Создание inquiry - зарегестрированый пользователь')
    def test_order_lme(self):
        browser.open_url("https://last-minute-essay.com/")
        browser.driver().maximize_window()
        lme.click_inquiry_button()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.sign_in(mail, pwd)
        fe.click_submit_inquiry_button()
        #all_site.close_Authorization_window()
        price = ph.change_inquiry_to_order('old_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    @allure.feature('Создание inquiry на LME')
    @allure.story('Создание inquiry - новый пользователь')
    def test_order_lme2(self):
        browser.open_url("https://last-minute-essay.com/")
        browser.driver().maximize_window()
        lme.click_inquiry_button()
        order_admin.choice_academic_level()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.i_am_new()
        fe.click_submit_inquiry_button()
        #all_site.click_done()
        price = ph.change_inquiry_to_order('new_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        #browser.close()

    # _________________________________________________DE________________________________
    @allure.feature('Создание inquiry на DE')
    @allure.story('Создание inquiry - зарегестрированый пользователь')
    def test_order_dw(self):
        browser.open_url("https://darwinessay.net")
        browser.driver().maximize_window()
        de.click_inquiry_button()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.sign_in(mail, pwd)
        all_site.scroll_down()
        fe.click_submit_inquiry_button()
        price = ph.change_inquiry_to_order('old_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)

    @allure.feature('Создание inquiry на DE')
    @allure.story('Создание inquiry - новый пользователь')
    def test_order_dw2(self):
        browser.open_url("https://darwinessay.net")
        browser.driver().maximize_window()
        de.click_inquiry_button()
        order_admin.choice_academic_level()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.i_am_new()
        all_site.scroll_down()
        fe.click_submit_inquiry_button()
        price = ph.change_inquiry_to_order('new_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)

    # _________________________________________________ET________________________________
    @allure.feature('Создание inquiry на ET')
    @allure.story('Создание inquiry - зарегестрированый пользователь')
    def test_order_et(self):
        browser.open_url("https://www.essaytigers.com/")
        browser.driver().maximize_window()
        all_site.scroll_down()
        main_page_et.click_inquiry_button()
        order_et.choice_subject_random(subject_list)
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.sign_in(mail, pwd)
        main_page_et.click_submit_inquiry_button()
        price = ph.change_inquiry_to_order('old_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)

    @allure.feature('Создание inquiry на ET')
    @allure.story('Создание inquiry - новый пользователь')
    def test_order_et2(self):
        browser.open_url("https://www.essaytigers.com/")
        browser.driver().maximize_window()
        all_site.scroll_down()
        main_page_et.click_inquiry_button()
        order_admin.choice_academic_level()
        order_et.choice_subject_random(subject_list)
        order_admin.set_topic(topic)
        order_admin.set_paper_details(paper_details)
        order_admin.i_am_new()
        main_page_et.click_submit_inquiry_button()
        price = ph.change_inquiry_to_order('new_client')
        order_steps.click_proceed_to_secure_payment_inquiry()
        order_steps.checking_price(price)
        browser.close()
        browser.quit_driver()