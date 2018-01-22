#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf8
import os

import allure
from selene.api import *
from selene.browsers import BrowserName

from General_pages import order_admin
from General_pages import modals, all_site
from General_pages import order_admin
from General_pages import order_steps
from Sites.AP import ap
from Sites.CW import cw
from Sites.DE import de
from Sites.DW import dw
from Sites.DW import main_page_dw
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
from data import mail, pwd, topic, paper_details, subject_list, additional_materials_list, preferred_writer_option_list, \
    Preferred_writer_ID
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
        print '\n ****************** START TEST CASE ************** \n'

    def teardown(m):
        print '\n ****************** END TEST KEYS ***************** \n'
        browser.driver().delete_all_cookies()
        browser.driver().close()



    #________________________________________________PH ________________________________
    @allure.feature('Создание заказа через админку клиента  PH')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_ph_with_admin(self):
        browser.open_url("https://www.paperhelp.org/")
        ph.click_sign_in()
        order_admin.set_mail_and_pass(mail, pwd)
        order_admin.click_create_order_button_admin_text()
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


    @allure.feature('Создание заказа через админку клиента EW')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_ew_with_admin(self):
        browser.open_url("https://evolutionwriters.com/")
        all_site.close_modal_start_window()
        ew.click_sign_in()
        order_admin.set_mail_and_pass(mail, pwd)
        #modals.modal_admin_auth_close()
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


    @allure.feature('Создание заказа через админку клиента WMP')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_wmp_with_admin(self):
        browser.open_url("https://www.writemypapers.org/")
        wmp.click_sign_in()
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


    @allure.feature('Создание заказа через админку клиента FE')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_fe2(self):
        browser.open_url("https://www.freshessays.com/")
        #browser.driver().maximize_window()
        fe.click_sign_in()
        fe.set_mail_and_pass(mail, pwd)
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


    @allure.feature('Создание заказа через админку клиента PW')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_pw2(self):
        browser.open_url("https://www.paperwritings.com/")
        pw.click_sign_in()
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
        order_admin.choice_option_preferred_writer(preferred_writer_option_list, Preferred_writer_ID)
        order_admin.choice_payment_system()
        price = order_steps.submit_proceed_to_secure_payment()
        #modals.modal_upgrade_order()
        order_steps.checking_price(price)


    @allure.feature('Создание заказа через админку клиента MAE')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_mae2(self):
        browser.open_url("https://myadmissionsessay.com/")
        mae.click_sign_in()
        order_admin.set_mail_and_pass(mail, pwd)
        # modals.modal_admin_auth_close()
        order_admin.click_create_order_button_admin()
        order_admin.choice_academic_level()
        order_admin.choice_type_of_paper_essays()
        order_admin.choice_subject_random()
        order_admin.set_topic(topic)
        #order_admin.set_single_or_double_spaced()
        order_admin.set_paper_details_LI()
        #order_admin.set_number_of_pages_random()
        order_admin.set_number_of_slides()
        order_admin.choice_paper_format_random_step_inquiry()
        order_admin.set_number_of_sources()
        order_admin.choice_additional_materials(additional_materials_list)
        order_admin.choice_Plagiarism_report()
        order_admin.choice_Abstract_page()
        order_admin.choice_VIP_customer_sevice()
        order_admin.choice_option_preferred_writer(preferred_writer_option_list, Preferred_writer_ID)
        order_admin.choice_payment_system()
        price = order_steps.submit_proceed_to_secure_payment()
        #modals.modal_upgrade_order()
        order_steps.checking_price(price)


    @allure.feature('Создание заказа через админку клиента EP')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_ep2(self):
        browser.open_url("https://essaypedia.com/")
        ep.click_sign_in()
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


    @allure.feature('Создание заказа через админку клиента PDN')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_pdn2(self):
        browser.open_url("https://admin.paperduenow.com")
        all_site.close_modal_start_window()
        #pdn.click_sign_in()                   while A/b test go to admin.paperduenow.com page
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


    @allure.feature('Создание заказа через админку клиента 1WS')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_1ws2(self):
        browser.open_url("https://1ws.com/")
        ws.click_sign_in()
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
        price = order_steps.click_proceed_to_secure_payment_inquiry()
        modals.modal_upgrade_order()
        order_steps.checking_price(price)


    @allure.feature('Создание заказа через админку клиента EE')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_ee(self):
        browser.open_url("https://expert-editing.org/")
        ee.click_sign_in()
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


    @allure.feature('Создание заказа через админку клиента FH')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_fh2(self):
        browser.open_url("http://www.freelancehouse.co.uk/")
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


    @allure.feature('Создание заказа через админку клиента LME')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_lme2(self):
        browser.open_url("https://last-minute-essay.com/")
        lme.click_sign_in()
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


    @allure.feature('Создание заказа через админку клиента UE')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_ue2(self):
        browser.open_url("http://unitedessays.com/")
        ue.click_sign_in()
        ue.set_mail_and_pass(mail, pwd)
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


    @allure.feature('Создание заказа через админку клиента DE')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_DE2(self):
        browser.open_url("https://darwinessay.net/")
        de.click_sign_in()
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


    @allure.feature('Создание заказа через админку клиента EA')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_ea2(self):
        browser.open_url("https://essays.agency/")
        main_page_ea.login()
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


    @allure.feature('Создание заказа через админку клиента ET')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_et2(self):
        browser.open_url("https://www.essaytigers.com")
        main_page_et.click_sign_in()
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


    @allure.feature('Создание заказа через админку клиента PM')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_pm2(self):
        browser.open_url("https://papersmaster.com/")
        main_page_pm.click_sign_in()
        order_admin.set_mail_and_pass(mail, pwd)
        #modals.modal_admin_auth_close()
        order_admin.click_create_order_button_admin()
        order_pm.choice_type_of_paper_essays()
        order_pm.choice_subject_random(subject_list)
        order_admin.set_topic(topic)
        order_admin.set_paper_details_LI()
        order_pm.choice_paper_format_random_step_inquiry()
        order_pm.choice_additional_materials(additional_materials_list)
        order_pm.choice_deadline()
        order_pm.choice_payment_system()
        price = order_pm.click_proceed_to_secure_payment_inquiry()
        #modals.modal_upgrade_order()
        order_steps.checking_price(price)

    @allure.feature('Создание заказа через админку клиента EST')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_est(self):
        browser.open_url("https://essaystone.com/")
        main_page_est.click_sign_in()
        order_admin.set_mail_and_pass(mail, pwd)
        modals.modal_admin_auth_close()
        order_admin.click_create_order_button_admin()
        order_pm.choice_type_of_paper_essays()
        order_pm.choice_subject_random(subject_list)
        order_admin.set_topic(topic)
        order_admin.set_paper_details_LI()
        order_pm.choice_paper_format_random_step_inquiry()
        order_pm.choice_additional_materials(additional_materials_list)
        order_pm.choice_deadline()
        #order_pm.choice_payment_system()
        price = order_pm.click_proceed_to_secure_payment_inquiry()
        #modals.modal_upgrade_order()
        order_steps.checking_price(price)

    #________________________________________________DW ________________________________
    @allure.feature('Создание заказа через админку клиента DW')
    @allure.story('Создание заказа - зарегестрированый пользователь')
    def test_order_dw2(self):
        browser.open_url("https://www.dissertationwritings.com/")
        main_page_dw.click_sign_in()
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

    @allure.feature('Создание заказа через админку клиента AP')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_ap(self):
        browser.open_url("https://www.affordable-papers.net/")
        ap.click_sign_in()
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

    @allure.feature('Создание заказа через админку клиента CW')
    @allure.story('Создание заказа - новый пользователь')
    def test_order_ap(self):
        browser.open_url("https://college-writers.com/")
        cw.click_sign_in()
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