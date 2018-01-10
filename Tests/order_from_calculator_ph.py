#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf8
import os
import shutil

import allure
from selene.api import *
from selene.browsers import BrowserName

from General_pages import order_steps, main_page
from Sites.PH import ph
from data import mail, pwd, topic, paper_details, Preferred_writer_ID

config.browser_name = BrowserName.PHANTOMJS
#config.hold_browser_open = True   # This options for a Chrome
config.desired_capabilities={}
config.timeout = 6
config.reports_folder = os.path.join(os.getcwd(), "screenshots")

class TestCalculator:
    driver = browser.driver()

    def setup(self):
        dir = os.getcwd()
        files = os.listdir(dir)
        for file in files:
            fullname = os.path.join(dir, file)
            if file == '.cache':
                shutil.rmtree(fullname)
        browser.open_url("https://www.paperhelp.org/")
        browser.driver().maximize_window()

    def teardown(self):
        #browser.close()
        pass

    ''''''

    @allure.feature('Create order, Type of paper  - Essays, Homework Help, Dissertation')
    @allure.story('Создание рандомного заказа - новый пользователь')
    def test_1_1(self):
        order_data = main_page.random_calculate_Essays_or_Homework_or_Dissertation()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Essays, Homework Help, Dissertation')
    @allure.story('Создание рандомного заказа - зарегестрированый пользователь')
    def test_1_2(self):
        order_data = main_page.random_calculate_Essays_or_Homework_or_Dissertation()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)


    @allure.feature('Create order, Type of paper  - Essays, Homework Help, Dissertation')
    @allure.story('Проверка дискаунта')
    def test_1_3(self):
        order_data = main_page.random_calculate_Essays_or_Homework_or_Dissertation()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        price = order_steps.order_price()
        order_steps.order_price_with_discount_70(price)
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Essays, Homework Help, Dissertation')
    @allure.story('Проверка отработки доступных чекбоксов')
    def test_1_4(self):
        order_data = main_page.random_calculate_Essays_or_Homework_or_Dissertation()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.check_abstract_page()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.check_plagiarism_report()
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        order_steps.check_VIP_customer_service()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Essays, Homework Help, Dissertation')
    @allure.story('Проверка My previous writer')
    def test_1_5(self):
        order_data = main_page.random_calculate_Essays_or_Homework_or_Dissertation()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        order_steps.choice_preferred_writer(Preferred_writer_ID)
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Essays, Homework Help, Dissertation')
    @allure.story('Проверка Additional Materials и Single Spaced')
    def test_1_6(self):
        order_data = main_page.random_calculate_Essays_or_Homework_or_Dissertation()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.choice_additional_materials()
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.choice_single_spaced()
        order_steps.set_number_of_pages_random()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Essays, Homework Help, Dissertation')
    @allure.story('Проверка Advanced regular writer)')
    def test_1_7(self):
        order_data = main_page.random_calculate_Essays_or_Homework_or_Dissertation()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        order_steps.choice_regular_writer()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Essays, Homework Help, Dissertation')
    @allure.story('Проверка дискаунта + TOP writer: Fulfilled by top 10 writers')
    def test_1_8(self):
        order_data = main_page.random_calculate_Essays_or_Homework_or_Dissertation()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        order_steps.choice_regular_writer()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    ##############————————————————- Admissions ——————————————— ##############

    @allure.feature('Create order, Type of paper  - Admission')
    @allure.story('Создание рандомного заказа тип работы Admission - зарегестрированый пользователь')
    def test_2_1(self):
        main_page.random_calculate_admissions()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.set_job_title_and_reasons()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Admission')
    @allure.story('Создание рандомного заказа тип работы Admission - новый пользователь ')
    def test_2_2(self):
        main_page.random_calculate_admissions()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_job_title_and_reasons()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Admission')
    @allure.story('Проверка дискаунта тип работы Admission')
    def test_2_3(self):
        order_data = main_page.random_calculate_admissions()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_job_title_and_reasons()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        price = order_steps.order_price()
        order_steps.order_price_with_discount_70(price)
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Admission')
    @allure.story('Проверка отработки доступных чекбоксов тип работы Admission')
    def test_2_4(self):
        order_data = main_page.random_calculate_admissions()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.set_job_title_and_reasons()
        order_steps.check_abstract_page()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.check_plagiarism_report()
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        order_steps.check_VIP_customer_service()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Admission')
    @allure.story('Проверка My previous writer тип работы Admission')
    def test_2_5(self):
        order_data = main_page.random_calculate_admissions()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_job_title_and_reasons()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        order_steps.choice_preferred_writer(Preferred_writer_ID)
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Admission')
    @allure.story('Проверка Additional Materials и Single Spaced тип работы Admission')
    def test_2_6(self):
        order_data = main_page.random_calculate_admissions()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.set_job_title_and_reasons()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.choice_additional_materials()
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.choice_single_spaced()
        order_steps.set_number_of_pages_random()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Admission')
    @allure.story('Проверка Advanced regular writer тип работы Admission')
    def test_2_7(self):
        order_data = main_page.random_calculate_admissions()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_job_title_and_reasons()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        order_steps.choice_regular_writer()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)


    @allure.feature('Create order, Type of paper  - Admission')
    @allure.story('Проверка дискаунта + TOP writer: Fulfilled by top 10 writers тип работы Admission')
    def test_2_8(self):
        order_data = main_page.random_calculate_admissions()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_job_title_and_reasons()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        order_steps.choice_regular_writer()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

        ##############————————————————- Problems ——————————————— ##############

    @allure.feature('Create order, Type of paper  - Problems')
    @allure.story('Создание рандомного заказа тип работы Problems - зарегестрированый пользователь')
    def test_3_1(self):
        main_page.random_calculate_problems()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_problems_random()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Problems')
    @allure.story('Создание рандомного заказа тип работы Problems - новый пользователь')
    def test_3_2(self):
        main_page.random_calculate_problems()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_problems_random()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)


    @allure.feature('Create order, Type of paper  - Problems')
    @allure.story('Проверка дискаунта тип работы Problems')
    def test_3_3(self):
        order_data = main_page.random_calculate_problems()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_problems_random()
        price = order_steps.order_price()
        order_steps.order_price_with_discount_70(price)
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)


    @allure.feature('Create order, Type of paper  - Problems')
    @allure.story('Проверка отработки доступных чекбоксов тип работы Problems')
    def test_3_4(self):
        order_data = main_page.random_calculate_problems()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_problems_random()
        order_steps.check_VIP_customer_service()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)


    @allure.feature('Create order, Type of paper  - Problems')
    @allure.story('Проверка Additional Materials и Single Spaced тип работы Problems')
    def test_3_5(self):
        order_data = main_page.random_calculate_problems()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.choice_additional_materials()
        order_steps.click_go_to_step3()
        order_steps.choice_single_spaced()
        order_steps.set_problems_random()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Problems')
    @allure.story('Проверка Advanced regular writer тип работы Problems')
    def test_3_6(self):
        order_data = main_page.random_calculate_problems()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_problems_random()
        order_steps.choice_regular_writer()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)


    @allure.feature('Create order, Type of paper  - Problems')
    @allure.story('Проверка дискаунта + TOP writer: Fulfilled by top 10 writers тип работы Problems')
    def test_3_7(self):
        order_data = main_page.random_calculate_problems()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_problems_random()
        order_steps.choice_regular_writer()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)


    ##############————————————————- Question  ——————————————— ##############

    @allure.feature('Create order, Type of paper  - Question')
    @allure.story('Создание рандомного заказа тип работы Question&Problems - зарегестрированый пользователь')
    def test_4_1(self):
        main_page.random_calculate_question()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_questions_random()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Question')
    @allure.story('Создание рандомного заказа тип работы Question&Problems - новый пользователь')
    def test_4_2(self):
        main_page.random_calculate_question()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_questions_random()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Question')
    @allure.story('Проверка дискаунта тип работы Question')
    def test_4_3(self):
        order_data = main_page.random_calculate_question()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_questions_random()
        price = order_steps.order_price()
        order_steps.order_price_with_discount_70(price)
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)


    @allure.feature('Create order, Type of paper  - Question')
    @allure.story('Проверка отработки доступных чекбоксов тип работы Question')
    def test_4_4(self):
        order_data = main_page.random_calculate_question()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_questions_random()
        order_steps.check_VIP_customer_service()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Question')
    @allure.story('Проверка My previous writer тип работы Question')
    def test_4_5(self):
        order_data = main_page.random_calculate_question()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_questions_random()
        order_steps.choice_preferred_writer(Preferred_writer_ID)
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Question')
    @allure.story('Проверка Additional Materials и Single Spaced тип работы Question')
    def test_4_6(self):
        order_data = main_page.random_calculate_question()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.choice_additional_materials()
        order_steps.click_go_to_step3()
        order_steps.choice_single_spaced()
        order_steps.set_questions_random()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Question')
    @allure.story('Проверка Advanced regular writer тип работы Question')
    def test_4_7(self):
        order_data = main_page.random_calculate_question()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_questions_random()
        order_steps.choice_regular_writer()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)


    @allure.feature('Create order, Type of paper  - Question')
    @allure.story('Проверка дискаунта + TOP writer: Fulfilled by top 10 writers тип работы Question')
    def test_4_8(self):
        order_data = main_page.random_calculate_question()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.click_go_to_step3()
        order_steps.set_questions_random()
        order_steps.choice_regular_writer()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)


    ##############————————————————- Typing  ——————————————— ##############

    @allure.feature('Create order, Type of paper  - Typing')
    @allure.story('Создание рандомного заказа - новый пользователь')
    def test_5_1(self):
        order_data = main_page.random_calculate_other_typing()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.varification_typing_order()
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Typing')
    @allure.story('Создание рандомного заказа - зарегестрированый пользователь')
    def test_5_2(self):
        order_data = main_page.random_calculate_other_typing()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.varification_typing_order()
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Typing')
    @allure.story('Проверка дискаунта')
    def test_5_3(self):
        order_data = main_page.random_calculate_other_typing()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.varification_typing_order()
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        price = order_steps.order_price()
        order_steps.order_price_with_discount_70(price)
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Typing')
    @allure.story('Проверка отработки доступных чекбоксов')
    def test_5_4(self):
        order_data = main_page.random_calculate_other_typing()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.check_abstract_page()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.varification_typing_order()
        order_steps.check_plagiarism_report()
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        order_steps.check_VIP_customer_service()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Typing')
    @allure.story('Проверка My previous writer')
    def test_5_5(self):
        order_data = main_page.random_calculate_other_typing()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.varification_typing_order()
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        order_steps.choice_preferred_writer(Preferred_writer_ID)
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Typing')
    @allure.story('Проверка Additional Materials и Single Spaced')
    def test_5_6(self):
        order_data = main_page.random_calculate_other_typing()
        order_steps.sign_in(mail, pwd)
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.varification_typing_order()
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.choice_single_spaced()
        order_steps.set_number_of_pages_random()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Typing')
    @allure.story('Проверка Advanced regular writer)')
    def test_5_7(self):
        order_data = main_page.random_calculate_other_typing()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.varification_typing_order()
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        order_steps.choice_regular_writer()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)

    @allure.feature('Create order, Type of paper  - Typing')
    @allure.story('Проверка дискаунта + TOP writer: Fulfilled by top 10 writers')
    def test_5_8(self):
        order_data = main_page.random_calculate_other_typing()
        order_steps.i_am_new()
        ph.choice_subject_random()
        order_steps.choice_paper_format()
        order_steps.set_sources_random()
        order_steps.set_topic(topic)
        order_steps.set_paper_details(paper_details)
        order_steps.varification_typing_order()
        order_steps.click_go_to_step3()
        order_steps.set_number_of_slides()
        order_steps.set_number_of_pages_random()
        order_steps.choice_regular_writer()
        price = order_steps.order_price()
        order_steps.click_proceed_to_secure_payment()
        order_steps.checking_price(price)



