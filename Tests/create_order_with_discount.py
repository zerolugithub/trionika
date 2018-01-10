#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf8
import os

import allure
from DE import de
from EST import order_est
from ET import main_page_et
from ET import order_et
from PH import ph
from PM import main_page_pm
from PM import order_pm
from WMP import wmp
from selene.api import *
from selene.browsers import BrowserName

from General_pages import order_steps, all_site
from Sites.FE import fe
from data import mail, pwd, topic, paper_details

#import httplib2
config.browser_name = BrowserName.PHANTOMJS
config.hold_browser_open = True   # This options for a Chrome
config.desired_capabilities={}
config.timeout = 10
config.reports_folder = os.path.join(os.getcwd(), "screenshots")

class Test_Create_Order:
    driver = browser.driver()

    def setup_module(m):
        config.browser_name = BrowserName.PHANTOMJS
        browser.driver().delete_all_cookies()
    def teatdown(self):
        browser.close()

    #________________________________________________PH ________________________________
    @allure.feature('Создание заказа на PH')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_ph2(self):
        browser.open_url("https://www.paperhelp.org/")
        browser.driver().maximize_window()
        ph.click_discount_button_on_header()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_discount_button()
        price_with_discount = order_steps.order_price_with_discount_5(price)
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price_with_discount)


    @allure.feature('Создание заказа на PH')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_ph(self):
        browser.open_url("https://www.paperhelp.org/")
        browser.driver().maximize_window()
        ph.click_discount_button_on_header()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_discount_button()
        price_with_discount = order_steps.order_price_with_discount_5(price)
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price_with_discount)

    # _________________________________________________WMP ________________________________
    @allure.feature('Создание заказа на WMP')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_wmp(self):
        browser.open_url("https://www.writemypapers.org/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        wmp.click_discount_button_on_header()
        order_steps.i_am_new()
        wmp.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_discount_button()
        price_with_discount = order_steps.order_price_with_discount_15(price)
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price_with_discount)

    @allure.feature('Создание заказа на WMP')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_wmp2(self):
        browser.open_url("https://www.writemypapers.org/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        wmp.click_discount_button_on_header()
        order_steps.sign_in(mail, pwd)
        wmp.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_discount_button()
        price_with_discount = order_steps.order_price_with_discount_15(price)
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price_with_discount)


    # _________________________________________________FE ________________________________
    @allure.feature('Создание заказа на FE')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_fe(self):
        browser.open_url("https://www.freshessays.com/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        fe.click_discount_button_on_header()
        fe.i_am_new()
        order_steps.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_discount_button()
        price_with_discount = order_steps.order_price_with_discount_7(price)
        order_steps.click_proceed_to_secure_payment()
        all_site.close_modal_upgrade_now()
        order_steps.checking_price(price_with_discount)

    @allure.feature('Создание заказа на FE')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_fe2(self):
        browser.open_url("https://www.freshessays.com/")
        browser.driver().maximize_window()
        #all_site.close_modal_start_window()
        fe.click_discount_button_on_header()
        order_steps.sign_in(mail, pwd)
        order_steps.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_discount_button()
        price_with_discount = order_steps.order_price_with_discount_7(price)
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price_with_discount)


# ________________________________________________DW ________________________________
    @allure.feature('Создание заказа на DW')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_dw(self):
        browser.open_url("https://darwinessay.net/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        de.click_discount_button_on_header()
        order_steps.i_am_new()
        order_steps.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_pages(5)
        price = order_steps.order_price()
        order_steps.click_discount_button()
        price_with_discount = order_steps.order_price_with_discount_10(price)
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price_with_discount)


    @allure.feature('Создание заказа на DW')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_dw2(self):
        browser.open_url("https://darwinessay.net/")
        browser.driver().maximize_window()
        all_site.close_modal_start_window()
        de.click_discount_button_on_header()
        order_steps.sign_in(mail, pwd)
        order_steps.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_pages(5)
        price = order_steps.order_price()
        order_steps.click_discount_button()
        price_with_discount = order_steps.order_price_with_discount_10(price)
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price_with_discount)


    # ________________________________________________ET ________________________________
    @allure.feature('Создание заказа на ET')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_et(self):
        browser.open_url("https://www.essaytigers.com")
        browser.driver().maximize_window()
        main_page_et.proceed_to_order()
        main_page_et.i_am_new()
        order_et.choice_subject_random()
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
    def test_order_et2(self):
        browser.open_url("https://www.essaytigers.com")
        browser.driver().maximize_window()
        main_page_et.proceed_to_order()
        main_page_et.sign_in(mail, pwd)
        order_et.choice_subject_random()
        order_et.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_et.click_proceed_to_secure_payment()
        order_steps.checking_price(price)


    # ________________________________________________PM ________________________________
    @allure.feature('Создание заказа на PM')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_pm(self):
        browser.open_url("https://papersmaster.com/")
        browser.driver().maximize_window()
        main_page_pm.proceed_to_order()
        order_pm.choice_subject_random()
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
    def test_order_pm2(self):
        browser.open_url("https://papersmaster.com/")
        browser.driver().maximize_window()
        main_page_pm.proceed_to_order()
        order_pm.choice_subject_random()
        order_pm.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_pm.login_on_order_page(mail, pwd)
        price = order_est.order_price()
        order_pm.click_proceed_to_secure_payment()
        order_steps.checking_price(price)
        browser.close()

