# coding: utf8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import httplib
import random
import string
import allure
import pytest
import requests
import selene
from selene import driver
from selene import tools
from selene.conditions import text, visible
from selene.api import *
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from data import discount_error, discount, paypalLogin, paypalPass
from selenium import webdriver


        #####   First step ##########
from tools import scrollDown


@allure.step('Создание рандомного email')
def random_mail():
    random_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(8)])
    mail = str(random_string) + '@' + str("Autotest.test")
    return mail


@allure.step('Заполнение формы для регистрации нового пользователя')
def i_am_new():
    time.sleep(1)
    s(by.xpath('//li[@tab-target="_create_client"]/a')).click()
    s('[name="first_name"]').set_value('AutoTest')
    s('[name="last_name"]').set_value('test')
    s('[name="email"]').set_value(random_mail())
    s('[name="phone_number"]').set_value('123123123')
    time.sleep(1)
    s('#butt_next_2').click()

@allure.step('Заполнение формы для регистрации нового пользователя')
def i_am_new_for_pid():
    time.sleep(1)
    s(by.xpath('//li[@tab-target="_create_client"]/a')).click()
    s('[name="first_name"]').set_value('Autotest')
    s('[name="last_name"]').set_value('Test')
    s('[name="email"]').set_value(random_mail())
    s('[name="phone_number"]').set_value('123123123')
    time.sleep(1)
    s('#butt_next_2').click()

@allure.step('Заполнение формы для регистрации старого пользователя')
def sign_in(email, pwd):
    time.sleep(1)
    s(by.xpath('//li[@tab-target="_client_login"]/a')).click()
    s('[name="email_reg"]').set_value(email)
    s('#password_reg').set_value(pwd)
    s('#butt_next_2').click()


@allure.step('Функционал "Forgot your password?"')
def click_forgot_password(mail):
    s('.password-forgot').click()
    s(by.xpath('//div[@class="form-block"]/input')).set_value(mail)
    s('.btn.btn-primary.btn-extra').click()


    #####   Second step ##########


### Choice random type of paper: Essays or Homework Help or Dissertation
@allure.step('Случайный выбор Type of paper  - Essays, Homework Help, Dissertation , Admissions')
def choice_randon_type_of_paper():
    a = str(random.randint(1, 3))
    if a == 1:
        count = str(random.randint(1, 24))
    elif a == 2:
        count = str(random.randint(1, 8))
    else:
        count = str(random.randint(1, 9))
    type_of_paper = s(by.xpath('.//select[@id="type_of_paper"]/optgroup[' + a + ']/option[' + count + ']'))
    type_of_paper.click()

@allure.step('Выбираем случайны  Academic level')
def choice_randon_academic_level():
    a = str(random.randint(1, 3))
    s(by.xpath('.//div[@class="block-9 re-03"]/div/div[' + a + ']')).click()
    time.sleep(2)


@allure.step('Выбираем случайны  Subject')
def choice_subject_random():
    n = str(random.randint(2, 69))
    time.sleep(3)
    s(by.xpath('//div/input[@id="subject_autocomplete"]')).click()
    s(by.xpath('//li[@class="ui-menu-item"][' + n + ']')).click()

@allure.step('Выбираем случайны  Paper Format')
def choice_paper_format_random_step():
    time.sleep(1)
    n = str(random.randint(1, 5))
    s(by.xpath('.//div[@id="paper_format_block"]/div[' + n + ']')).click()

@allure.step('Выбираем случайны  Paper Format')
def choice_paper_format():
    s('#paper_formatAPA_label').click()

# Fields for Type of Paper - "Admisiions"
@allure.step('В зависимости от Type of paper заполняем поля (Type of institution + Institution (program) name или  Job title or industry segment + Reasons for applying)')
def set_job_title_and_reasons():
    if s('[name="institution"]').is_displayed():
        n = str(random.randint(2, 8))
        s(by.xpath('.//*[@id="_type_of_institution"]/div[2]/select/option[' + n + ']')).click()
        s('[name="institution"]').set_value('Test')
    else:
        s('[name="reasons_for_applying"]').set_value('Test')
        s('[name="job_title_or_industry"]').set_value('Test')


@allure.step('Устанавливаем чекбокс на  Add an Abstract page to my paper ')
def check_abstract_page():
    s('[name="abstract_page"]').click()


@allure.step('Устанавливаем чекбокс на  I want to receive official Plagiarism report ')
def check_plagiarism_report():
    s('[name="plagiarism_report"]').click()


@allure.step('Генерируем случайное число и вводим в поле Sources')
def set_sources_random():
    n = random.randint(1, 10)
    s('[name="sources_needed"]').click().set_value(n)


@allure.step('Заполняем поле Topic - Test')
def set_topic(topic):
    s('[name="topic"]').set_value(topic)


@allure.step('Заполняем поле Paper Details: - IT Test Autamation ')
def set_paper_details(paper_details):
    s('[name="paper_details"]').set_value(paper_details)


@allure.step('Нажимаем на кнопку   «Go to step 3»')
def click_go_to_step3():
    s('#butt_next_3').click()


@allure.step('Выбираем рандомно опцию  Additional Materials:')
def choice_additional_materials():
    n = str(random.randint(1, 3))
    s(by.xpath('//div[@class="button-group button-group-justified radio-group cascade-group"]/div[' + n + ']')).click()


#########  Third step ##############

def type_of_service():
    pass


def academic_level():
    pass


@allure.step('Устанавливаем чекбокс на I want to order VIP customer servic')
def check_VIP_customer_service():
    s('[name="top_priority"]').click()


@allure.step('Генерируем случайное число и вводим в поле Number of Pages')
def set_number_of_pages_random():
    n = random.randint(1, 20)
    s('#input_pages').set_value(n)
    while True:
        try:
            alert = s(by.xpath('//div[@class="form-alert alert fade in"][@error="pages"]')).text
        except TimeoutException:
            return True
        else:
            alert = s(by.xpath('//div[@class="form-alert alert fade in"][@error="pages"]')).text
            print alert
            if len(alert)==69:
                count = alert.split(' ')[-9]
                s('#input_pages').set_value(count)
            elif len(alert)==83:
                count = alert.split(' ')[-10]
                s('#input_pages').set_value(count)
            else:
                "Input pages has error !!! "
                break

@allure.step('Вводим случайное число в поле Number of Pages')
def set_pages(count):
    s('#input_pages').set_value(count)
    while True:
        try:
            alert = s(by.xpath('//div[@class="form-alert alert fade in"][@error="pages"]')).text
        except TimeoutException:
            return True
        else:
            alert = s(by.xpath('//div[@class="form-alert alert fade in"][@error="pages"]')).text
            print alert
            if len(alert)==69:
                count = alert.split(' ')[-9]
                s('#input_pages').set_value(count)
            elif len(alert)==83:
                count = alert.split(' ')[-10]
                s('#input_pages').set_value(count)
            else:
                "Input pages has error !!! "
                break

@allure.step('Генерируем случайное число и вводим в поле Number of slides')
def set_number_of_slides():
    n = random.randint(1, 10)
    s('._slides.form-input').set_value(n)

@allure.step('Вводим в поле Number of slides число слайдов')
def set_number_of_slides_count(count):
    s('[name="slides"]').set_value(count)

@allure.step('Вводим в поле Problems количество проблем')
def set_problems(problems):
    s('[name="problems"]').set_value(problems)
    if s(by.xpath('//div[@class="form-alert alert fade in" ]')).is_displayed():
        alert = s(by.xpath('//div[@class="form-alert alert fade in" ]')).text
        count = alert.split(' ')[-1]
        count = int(count[0:-1])
        s('[name="problems"]').set_value(count)
        time.sleep(1)
    else:
        pass

@allure.step('Генерируем случайное число и вводим в поле Problems ')
def set_problems_random():
    n = random.randint(1, 25)
    s('[name="problems"]').set_value(n)
    if s(by.xpath('//div[@class="form-alert alert fade in" ]')).is_displayed():
        alert = s(by.xpath('//div[@class="form-alert alert fade in" ]')).text
        count = alert.split(' ')[-1]
        count = int(count[0:-1])
        s('[name="problems"]').set_value(count)
        time.sleep(1)
    else:
        pass

@allure.step('Генерируем случайное число и вводим в поле Questions')
def set_questions_random():
    n = random.randint(1, 30)
    s('[name="questions"]').set_value(n)

@allure.step('Вводим в поле Questions количество вопросов')
def set_questions(questions):
    s('[name="questions"]').set_value(questions)

@allure.step('Выбор опции Single Spaced')
def choice_single_spaced():
    s('#spacingSING_label').click()


def deadline():
    pass


def choice_payment_system():
    pass


def preferred_writer():
    pass


def checking_deadline_for_question():
    pass


def click_discount_button():
    s('#disc_check').click()


def set_discount(discount):
    s('#have_disc').click()
    s('[name="discount_code"]').set_value(discount)
    s('#disc_check').click()
    time.sleep(2)
    '''if int(float((order_price()))) <= 30:
        s(by.xpath('.//div[@class="block-6 class-empty form-block discount-block-alert"]/div')).should(
            be.visible).assure(text(discount_error))
    else:
        print 'Price over 30$ - create order with discount ' '''


@allure.step('Запоминаем значение поля TOTAL PRICE')
def order_price():
    time.sleep(2)
    price = s('#appr_price_step3').text
    price = price[1:]
    return price



def order_price_with_discount_5(old_price):
    time.sleep(2)
    price_with_discount = (float(old_price) * 0.95) - 0.001
    price_with_discount = round(price_with_discount, 2)
    price_with_discount = '$' + str(price_with_discount)
    s('#appr_price_step3').should_have(text(price_with_discount))
    price_with_discount = price_with_discount[1:]
    return price_with_discount

def order_price_with_discount_7(old_price):
    time.sleep(2)
    price_with_discount = (float(old_price) * 0.93) - 0.001
    price_with_discount = round(price_with_discount, 2)
    price_with_discount = '$' + str(price_with_discount)
    s('#appr_price_step3').should_have(text(price_with_discount))
    price_with_discount = price_with_discount[1:]
    return price_with_discount

def order_price_with_discount_10(old_price):
    time.sleep(2)
    price_with_discount = (float(old_price) * 0.90) - 0.001
    price_with_discount = round(price_with_discount, 2)
    price_with_discount = '$' + str(price_with_discount)
    s('#appr_price_step3').should_have(text(price_with_discount))
    price_with_discount = price_with_discount[1:]
    return price_with_discount

def order_price_with_discount_15(old_price):
    time.sleep(2)
    price_with_discount = (float(old_price) * 0.85) - 0.001
    price_with_discount = round(price_with_discount, 2)
    price_with_discount = '$' + str(price_with_discount)
    s('#appr_price_step3').should_have(text(price_with_discount))
    price_with_discount = price_with_discount[1:]
    return price_with_discount

@allure.step(' Ввести скидочный код - jaredtest, проверить стоимость.')
def order_price_with_discount_70(price):
    price = float(price)
    s('#have_disc').click()
    s('[name="discount_code"]').set_value(discount)
    s('#disc_check').click()
    time.sleep(2)
    while price < 30:
        if s('._questions_incr.right_incr.button.button-default').is_displayed():
            s('._questions_incr.right_incr.button.button-default').click()
            time.sleep(1)
            price = s('#appr_price_step3').text
            price = float(price[1:])
            s('#disc_check').click()
            time.sleep(3)
        elif s('._problems_incr.right_incr.button.button-default').is_displayed():
            s('._problems_incr.right_incr.button.button-default').click()
            time.sleep(1)
            price = s('#appr_price_step3').text
            price = float(price[1:])
            s('#disc_check').click()
            time.sleep(3)
        else:
            s('[name="pages"]').set_value(3)
            time.sleep(1)
            price = s('#appr_price_step3').text
            price = float(price[1:])
            s('#disc_check').click()
            time.sleep(3)
    price_with_discount = ((float(price)) * 0.90) - 0.001
    price_with_discount = round(price_with_discount, 2)
    price_with_discount = '$' + str(price_with_discount)
    s('#appr_price_step3').should_have(text(price_with_discount))
    price_with_discount = price_with_discount[1:]

    return price_with_discount


@allure.step(' Нажать на кнопку «My previous writer», ввести Writers ID: 263529979 ')
def choice_preferred_writer(id):
    if s('#preferred_writerMY_label').is_enabled():
        print 'Option «My previous writer» Not available'
    else:
        s('#preferred_writerMY_label').click()
        s('[name="previous_writer"]').set_value(id)
        time.sleep(3)


@allure.step(' Нажать на кнопку «Advanced regular writer»')
def choice_regular_writer():
    s('#preferred_writerADV_REG_label').click()

@allure.step(' Нажать на кнопку «TOP writer: Fulfilled by top 10 writers»')
def choice_TOP_writer():
    s('#preferred_writerADV_REG_label').click()

####### Payment #########

@allure.step(' Нажать на кнопку «Credit card»')
def choice_credit_card():
    s(by.xpath('.//*[@id="_choose_pay_system"]/div[2]/div/div[1]')).click()

@allure.step(' Нажать на кнопку «PayPal»')
def choice_PayPal():
    s(by.xpath('.//*[@id="_choose_pay_system"]/div[2]/div/div[2]')).click()

@allure.step(' Сравнение цены на заказе и на платежке')
def checking_price(price):
    time.sleep(20)
    title = selene.tools.get_driver().title
    title= browser.driver().title
    url = browser.driver().current_url
    if len(price)==7:
        p = price[:1] + ',' + price[1:]
    try:
        if title == 'PayPal Checkout - Create a PayPal account!':
            p = price[1:0]
            price = s(by.xpath('//*[@id="transactionCart"]/span[2]/format-currency/span')).assure(text(p))
            print 'The payment system is PayPal'
        elif title == 'PayPal Checkout - Log in':
            p = price[1:0]
            price = s(by.xpath('//*[@id="transactionCart"]/span[2]/format-currency/span')).assure(text(p))
            print 'The payment system is PayPal'
        elif title == 'Log in to your PayPal account':
            print "Sign in to your payment system account"
            s('#email').set_value(paypalLogin)
            s('#password').set_value(paypalPass)
            s('#btnLogin').click()
            time.sleep(1)
            p = price.replace('.',',')
            print p
            #actual  = '$' + p + ' USD'
            #print actual
            price = s('.formatCurrency.ng-isolate-scope').assure(text(p))
            print 'The payment system is PayPal' + p
        elif title == 'Log in to your account':
            print "Sign in to your payment system account"
            s('#email').set_value(paypalLogin)
            s('#password').set_value(paypalPass)
            s('#btnLogin').click()
            time.sleep(1)
            p = price.replace('.',',')
            print p
            #actual  = '$' + p + ' USD'
            #print actual
            price = s('.formatCurrency.ng-isolate-scope').assure(text(p))
            print 'The payment system is PayPal' + p
        elif title == 'PayPal':
            p = price[1:0]
            price = s(by.xpath('//*[@id="transactionCart"]/span[2]/format-currency/span')).assure(text(p))
            print 'The payment system is PayPal'
        elif title == 'Secure Order Payment':
            s('.currency_price').assure(text(price))
            print 'The payment system is Credit card'
            # add paypal ################
        elif 'paypal' in url:
            time.sleep(2)
            price = s(by.xpath('.//*[@id="multiitem1"]/ul[1]/li[1]/span[2]')).assure(text(price))
            print 'The payment system is paypal'
            ###########################
            # -------Avangate_________________________
        elif title == 'EssayStone': #and s(by.xpath('.//*[@id="order__sub__total__row"]/td/table/tbody/tr/td[2]/div[3]/span[3]')).is_displayed():
            time.sleep(2)
            '$' + price
            price = s(by.xpath('//span[@class="order__billing__total"]')).assure(text(price))   # //*[@id="order__finalTotalPrice"]/p/span/span[2]
        elif 'avangate' in url:
            time.sleep(2)
            price = s(by.xpath('//span[@class="order__billing__total"]')).assure(text(price))   # may be + $
            print 'The payment system is Avangate'
            #-------Bluesnap_________________________
        elif 'bluesnap' in url: #s('.pli-total>span').is_displayed():
            time.sleep(2)
            p = price[1:0]
            s('.pli-total>span').assure(text(p))
            print 'The payment system is BlueSnap'
        elif title == 'affordable-papers.net':
            price = s('#items_table > tbody > tr.even > td.price').text
            print 'The payment system is gate2shop' + price
        elif title == 'darwinessay.net':
            price = s('#items_table > tbody > tr.even > td.price').text
            print 'The payment system is gate2shop' + price
        else:
            print 'The order did not go to the payment page'
            s('.Error - The order did not go to the payment page').click()
            # DO STUFF
    except httplib.BadStatusLine:
        pass

@allure.step(' Нажать на кнопку "Proceed to secure payment" при создании заказа')
def click_proceed_to_secure_payment():
    s('#payment_button').click()
    time.sleep(5)


@allure.step(' Нажать на кнопку "Proceed to secure payment" при создании inquiry')
def click_proceed_to_secure_payment_inquiry():
    time.sleep(3)
    scrollDown()
    price = s('.price_strong.strong_price_order').text
    price = price[1:]
    s('#payment_button_admin').click()
    return price


@allure.step(' Нажать на кнопку "Proceed to secure payment" ')
def submit_proceed_to_secure_payment():
    time.sleep(5)
    price = s('.price_strong.strong_price_order').text
    price = price[1:]
    time.sleep(2)
    s('#payment_button_admin').submit().click()
    return price

def varification_typing_order():
    s(by.xpath('//div[@class="button-group button-group-justified radio-group cascade-group"]/div[@class="button-group active"]/label/div/span')).should_have(text('Needed, I will provide them later'))