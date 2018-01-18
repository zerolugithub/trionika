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
from tools import phantom_js_clean_up, config_browser, chrome_clean_up
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
        chrome_clean_up()



    #________________________________________________PH ________________________________
    @allure.feature('Создание заказа на PH')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_ph2(self):
        browser.open_url("https://www.paperhelp.org/")
        ph.proceed_to_order()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)


    @allure.feature('Создание заказа на PH')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_ph(self):
        browser.open_url("https://www.paperhelp.org/")
        ph.proceed_to_order()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    #_________________________________________________EW ________________________________
    @allure.feature('Создание заказа на EW')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_ew(self):
        browser.open_url("https://evolutionwriters.com/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        ew.proceed_to_order()
        order_steps.i_am_new()
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

    @allure.feature('Создание заказа на EW')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_ew2(self):
        browser.open_url("https://evolutionwriters.com/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        ew.proceed_to_order()
        order_steps.sign_in(mail, pwd)
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

    # _________________________________________________WMP ________________________________
    @allure.feature('Создание заказа на WMP')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_wmp(self):
        browser.open_url("https://www.writemypapers.org/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        wmp.proceed_to_order()
        order_steps.i_am_new()
        wmp.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Создание заказа на WMP')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_wmp2(self):
        browser.open_url("https://www.writemypapers.org/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        wmp.proceed_to_order()
        order_steps.sign_in(mail, pwd)
        wmp.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    # _________________________________________________FE ________________________________
    @allure.feature('Создание заказа на FE')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_fe(self):
        browser.open_url("https://www.freshessays.com/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        fe.proceed_to_order()
        fe.i_am_new()
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

    @allure.feature('Создание заказа на FE')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_fe2(self):
        browser.open_url("https://www.freshessays.com/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        fe.proceed_to_order()
        order_steps.sign_in(mail, pwd)
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

    # _________________________________________________PW ________________________________
    @allure.feature('Создание заказа на PW')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_pw(self):
        browser.open_url("https://www.paperwritings.com/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        pw.proceed_to_order()
        order_steps.i_am_new()
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

    @allure.feature('Создание заказа на PW')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_pw2(self):
        browser.open_url("https://www.paperwritings.com/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        pw.proceed_to_order()
        order_steps.sign_in(mail, pwd)
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

    # _________________________________________________MAE ________________________________
    @allure.feature('Создание заказа на MAE')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_mae(self):
        browser.open_url("https://myadmissionsessay.com/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        mae.proceed_to_order()
        order_steps.i_am_new()
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

    @allure.feature('Создание заказа на MAE')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_mae2(self):
        browser.open_url("https://myadmissionsessay.com/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        mae.proceed_to_order()
        order_steps.sign_in(mail, pwd)
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


    # _________________________________________________EP ________________________________
    @allure.feature('Создание заказа на EP')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_ep(self):
        browser.open_url("https://essaypedia.com/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        ep.proceed_to_order()
        order_steps.i_am_new()
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

    @allure.feature('Создание заказа на EP')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_ep2(self):
        browser.open_url("https://essaypedia.com/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        ep.proceed_to_order()
        order_steps.sign_in(mail, pwd)
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

    # _________________________________________________PDN ________________________________
    @allure.feature('Создание заказа на PDN')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_pdn(self):
        browser.open_url("https://paperduenow.com/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        pdn.proceed_to_order()
        order_steps.i_am_new()
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

    @allure.feature('Создание заказа на PDN')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_pdn2(self):
        browser.open_url("https://paperduenow.com/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        pdn.proceed_to_order()
        order_steps.sign_in(mail, pwd)
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

    # _________________________________________________1WS ________________________________
    @allure.feature('Создание заказа на 1WS')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_1ws(self):
        browser.open_url("https://1ws.com/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        ws.proceed_to_order()
        order_steps.i_am_new()
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

    @allure.feature('Создание заказа на 1WS')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_1ws2(self):
        browser.open_url("https://1ws.com/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        ws.proceed_to_order()
        order_steps.sign_in(mail, pwd)
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

    # _________________________________________________EE ________________________________
    @allure.feature('Создание заказа на EE')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_ee(self):
        browser.open_url("https://expert-editing.org/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        ee.proceed_to_order()
        order_steps.i_am_new()
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

    @allure.feature('Создание заказа на EE')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_ee2(self):
        browser.open_url("https://expert-editing.org/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        ee.proceed_to_order()
        order_steps.sign_in(mail, pwd)
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

    # _________________________________________________FH ________________________________
    @allure.feature('Создание заказа на FH')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_fh(self):
        browser.open_url("http://www.freelancehouse.co.uk/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        fh.proceed_to_order()
        order_steps.i_am_new()
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

    @allure.feature('Создание заказа на FH')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_fh2(self):
        browser.open_url("http://www.freelancehouse.co.uk/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        fh.proceed_to_order()
        order_steps.sign_in(mail, pwd)
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

    # _________________________________________________LME ________________________________
    @allure.feature('Создание заказа на LME')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_lme(self):
        browser.open_url("https://last-minute-essay.com/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        lme.proceed_to_order()
        order_steps.i_am_new()
        lme.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        all_site.close_modal_upgrade_now()
        order_steps.checking_price(price)

    @allure.feature('Создание заказа на LME')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_lme2(self):
        browser.open_url("https://last-minute-essay.com/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        lme.proceed_to_order()
        order_steps.sign_in(mail, pwd)
        lme.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        all_site.close_modal_upgrade_now()
        order_steps.checking_price(price)

    # _________________________________________________UE ________________________________
    @allure.feature('Создание заказа на UE')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_ue(self):
        browser.open_url("http://unitedessays.com/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        ue.proceed_to_order()
        ue.i_am_new()
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

    @allure.feature('Создание заказа на UE')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_ue2(self):
        browser.open_url("http://unitedessays.com/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        ue.proceed_to_order()
        order_steps.sign_in(mail, pwd)
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

# ________________________________________________DE ________________________________
    @allure.feature('Создание заказа на DE')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_DE(self):
        browser.open_url("https://darwinessay.net/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        de.proceed_to_order()
        order_steps.i_am_new()
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

    @allure.feature('Создание заказа на DE')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_DE2(self):
        browser.open_url("https://darwinessay.net/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        de.proceed_to_order()
        order_steps.sign_in(mail, pwd)
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

# ________________________________________________EA ________________________________
    @allure.feature('Создание заказа на EA')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_ea(self):
        browser.open_url("https://essays.agency/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        main_page_ea.login()
        all_site.close_Authorization_window()
        order_ea.new_order()
        order_ea.choice_subject_random()
        #order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        price = order_ea.order_price()
        order_ea.click_Proceed_to_Secure_Payment()
        all_site.close_modal_upgrade_now()
        order_steps.checking_price(price)
        #browser.close()

    @allure.feature('Создание заказа на EA')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_ea2(self):
        browser.open_url("https://essays.agency/")
        browser.driver().maximize_window()
        main_page_ea.sign_up()
        main_page_ea.click_register_button()
        all_site.close_Authorization_window()
        order_ea.new_order()
        order_ea.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        price = order_ea.order_price()
        order_ea.click_Proceed_to_Secure_Payment()
        all_site.close_modal_upgrade_now()
        order_steps.checking_price(price)

    # ________________________________________________ET ________________________________
    @allure.feature('Создание заказа на ET')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_et(self):
        browser.open_url("https://www.essaytigers.com")
        browser.driver().maximize_window()
        main_page_et.proceed_to_order()
        main_page_et.i_am_new()
        order_et.choice_subject_random(subject_list)
        order_et.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_et.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Создание заказа на ET')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_et2(self):
        browser.open_url("https://www.essaytigers.com")
        browser.driver().maximize_window()
        main_page_et.proceed_to_order()
        main_page_et.sign_in(mail, pwd)
        order_et.choice_subject_random(subject_list)
        order_et.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_et.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    # ________________________________________________EST ________________________________
    @allure.feature('Создание заказа на EST')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_est(self):
        browser.open_url("https://essaystone.com/")
        browser.driver().maximize_window()
        main_page_est.proceed_to_order()
        order_est.choice_subject_random()
        order_est.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_est.regigister()
        price = order_est.order_price()
        order_est.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Создание заказа на EST')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_est2(self):
        browser.open_url("https://essaystone.com/")
        browser.driver().maximize_window()
        main_page_est.proceed_to_order()
        order_est.choice_subject_random()
        order_est.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_est.login_on_order_page(mail, pwd)
        price = order_est.order_price()
        order_est.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

  # ________________________________________________PM ________________________________
    @allure.feature('Создание заказа на PM')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_pm(self):
        browser.open_url("https://papersmaster.com/")
        browser.driver().maximize_window()
        main_page_pm.proceed_to_order()
        order_est.choice_subject_random()
        order_pm.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_pm.regigister()
        price = order_est.order_price()
        order_pm.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Создание заказа на PM')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_pm2(self):
        browser.open_url("https://papersmaster.com/")
        browser.driver().maximize_window()
        main_page_pm.proceed_to_order()
        order_est.choice_subject_random()
        order_pm.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_pm.login_on_order_page(mail, pwd)
        price = order_est.order_price()
        order_pm.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    #________________________________________________DW ________________________________
    @allure.feature('Создание заказа на DW')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_dw2(self):
        browser.open_url("https://www.dissertationwritings.com/")
        browser.driver().maximize_window()
        dw.proceed_to_order()
        order_steps.sign_in(mail, pwd)
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

    @allure.feature('Создание заказа на DW')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_dw(self):
        browser.open_url("https://www.dissertationwritings.com/")
        browser.driver().maximize_window()
        dw.proceed_to_order()
        order_steps.i_am_new()
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

    #________________________________________________AP ________________________________
    @allure.feature('Создание заказа на AP')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_ap2(self):
        browser.open_url("https://www.affordable-papers.net/")
        browser.driver().maximize_window()
        ap.proceed_to_order()
        order_steps.sign_in(mail, pwd)
        ap.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        modals.modal_upgrade_order()
        order_steps.checking_price(price)

    @allure.feature('Создание заказа на AP')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_ap(self):
        browser.open_url("https://www.affordable-papers.net/")
        browser.driver().maximize_window()
        ap.proceed_to_order()
        order_steps.i_am_new()
        ap.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        modals.modal_upgrade_order()
        order_steps.checking_price(price)

    #________________________________________________CW ________________________________
    @allure.feature('Создание заказа на CW')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_steps_cw2(self):
        browser.open_url("https://college-writers.com/")
        browser.driver().maximize_window()
        cw.proceed_to_order()
        order_steps.sign_in(mail, pwd)
        cw.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        modals.modal_upgrade_order()
        order_steps.checking_price(price)

    @allure.feature('Создание заказа на CW')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_steps_cw(self):
        browser.open_url("https://college-writers.com/")
        browser.driver().maximize_window()
        cw.proceed_to_order()
        order_steps.i_am_new()
        cw.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        modals.modal_upgrade_order()
        order_steps.checking_price(price)
