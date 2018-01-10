# coding: utf8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string
import allure
import pytest
from selene.conditions import text
from selene.api import *
import time

from data import mail, pwd
@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s('#navigation-menu > nav > div.top-navigation > div > div > div:nth-child(4) > a').click()

@allure.step("Нажимаем на кнопку 'Order Now' ")
def click_order_now_button():
    s(by.xpath('.//a[text()="Order Now"]')).click()

@allure.step("Нажимаем на кнопку 'Proceed to Order' ")
def click_calculate_order_button():
    s('#calc_form > a').click()

@allure.step("Нажимаем на кнопку 'SAVE5NOW' ")
def click_discount_button():
    s('.container.text-center>a').click()

@allure.step("Нажимаем на кнопку 'Get Inquiry' ")
def click_inquiry_button():
    s('a[href="/inquiry.html"]').click()
    print '\nCreate inquiry on https://www.paperhelp.org/'

@allure.step('Нажимаем на главной странице кнопку Order')
def proceed_to_order():
    print 'Create order on PH'
    time.sleep(2)
    s('#navbar > ul > a').click()

@allure.step('Выбираем случайны  Subject')
def choice_subject_random():
    n = str(random.randint(2, 11))
    time.sleep(1)
    s('#subject_test').click()
    s(by.xpath('//li[@class="ui-menu-item"][' + n + ']')).click()
    #time.sleep(1)
    # subject = ss('subject_test')
    # subject.s(by.xpath('option[' + n + ']'))

@allure.step('Переход в админку клиента зарегестрированного пользователя')
def go_to_admin_after_order():
    browser.open_url("https://www.paperhelp.org/")
    s('.btn-sign-in').click()



@allure.step('Запомнить последний заказ в админке клиента')
def get_last_number_order():
    time.sleep(1)
    s(by.xpath('//span[@data-intro="Click on the order number to view your order."]/a')).click()
    order =  s('.content-header-holder>h1>span')
    order = order.text
    order = order[1:]
    return order

@allure.step('Нажать на кнопку Inquiry на главной странице')
def click_inquiry_button():
    print 'Create inquiry on PH'
    s('a[href="/inquiry.html"]').click()

@allure.step('Перевод Inquiry в Order')
def change_inquiry_to_order(client):
    time.sleep(1)
    # if s(by.xpath('//*[@id="verification_modal"]/div/div')).is_displayed():
    #     s('#close_varification_modal').click()

    if client == 'new_client':
        time.sleep(1)
        s('#close_varification_modal').click()
        s('body > div.introjs-helperLayer > div > div.introjs-tooltipbuttons > a').click()
        #s('#close_varification_modal').click()
        time.sleep(2)
    elif client == 'old_client':
        time.sleep(2)
        pass
    order_number = s(by.xpath('.//tbody/tr/td[1]/span')).text
    price = s(by.xpath('.//tbody/tr/td[5]')).text
    price = price[1:]
    s(by.xpath('.//tbody/tr/td/span/a/../../../td[9]/a')).click()
    print 'Current order is ' + order_number + ' and price ' + price + '$'
    time.sleep(10)
    return order_number


@allure.step('Нажать на кнопку с дискаунтом на главной странице')
def click_discount_button_on_header():
    s(by.xpath('.//*[@id="header-menu"]/div/div/a/span')).click()

@allure.step('Нажать на кнопку с дискаунтом на главной странице')
def sign_in():
    s(by.xpath('//a[@class="btn-sign-in"]')).click()
    s('#inputEmail3').send_keys(mail)
    s('#inputPassword3').send_keys(pwd)
    s('.btn.btn-default.btn-block.btn-login').click()

#class main_page(object):

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s('#navigation-menu > nav > div.top-navigation > div > div > div:nth-child(4) > a').click()

@allure.step("Нажимаем на кнопку 'Order Now' ")
def click_order_now_button():
    s(by.xpath('.//a[text()="Order Now"]')).click()

@allure.step("Нажимаем на кнопку 'Proceed to Order' ")
def click_calculate_order_button():
    s('#calc_form > a').click()

@allure.step("Нажимаем на кнопку 'SAVE5NOW' ")
def click_discount_button():
    s('.container.text-center>a').click()

@allure.step("Нажимаем на кнопку 'Get Inquiry' ")
def click_inquiry_button():
    browser.driver().execute_script(("window.scrollTo(0, document.body.scrollHeight);"))
    s('a[href="/inquiry.html"]').click()
    print '\nCreate inquiry on https://www.paperhelp.org/'



@allure.step('Создание рандомного заказа с калькулятора, Type of paper  - Essays, Homework Help, Dissertation ')
def random_calculate_Essays_or_Homework_or_Dissertation():
    a = str(random.randint(1, 3))
    if a == 1:
        count = str(random.randint(1, 24))
    elif a == 2:
        count = str(random.randint(1, 8))
    else:
        count = str(random.randint(1, 9))
    type_of_paper = s(by.xpath('.//select[@id="form_service_type"]/optgroup[' + a + ']/option[' + count + ']'))
    type_of_paper.click()
    # Choice random academic level
    a = str(random.randint(1, 3))
    academic_level = s(by.xpath('.//select[@id="form_academic_level"]/option[' + a + ']'))  #' + a + '
    academic_level.click()
    # Choice random deadline
    a = str(random.randint(1, 9))
    deadline = s(by.xpath('.//select[@id="form_deadline"]/option[' + a + ']'))
    deadline.click()
    # Choice random number of pages (max 10 pages)
    a = str(random.randint(1, 20))
    pages = s(by.xpath('.//select[@id="form_pages"]/option[' + a + ']'))
    pages.click()
    # Create dictionary order_data
    order_data = {'type_of_paper': type_of_paper.text,
                  'academic_level': academic_level.text,
                  'deadline': deadline.text,
                  'pages': pages.text}
    # Click order button
    s('#calc_form > a').click()
    return order_data


@allure.step('Создание рандомного заказа с калькулятора, Type of paper  - Аdmissions ')
def random_calculate_admissions():
    b = str(random.randint(1, 6))
    s(by.xpath('.//select[@id="form_service_type"]/optgroup[4]/option[' + b + ']')).click()
    # Choice deadline
    c = str(random.randint(1, 9))
    s(by.xpath('.//select[@id="form_deadline"]/option[' + c + ']')).click()
    # Choice number of pages
    d = str(random.randint(1, 10))
    s(by.xpath('.//select[@id="form_pages"]/option[' + d + ']')).click()
    # Click order button
    s('#calc_form > a').click()


@allure.step('Создание рандомного заказа с калькулятора, Type of paper  -  Problems" ')
def random_calculate_problems():
    s(by.xpath('.//select[@id="form_service_type"]/optgroup[5]/option[1]')).click()
    # Choice academic level
    b = str(random.randint(1, 3))
    s(by.xpath('.//select[@id="form_academic_level"]/option[' + b + ']')).click()
    # Choice deadline
    c = str(random.randint(1, 9))
    s(by.xpath('.//select[@id="form_deadline"]/option[' + c + ']')).click()
    # Choice number of pages
    d = str(random.randint(1, 10))
    s(by.xpath('.//select[@id="form_pages"]/option[' + d + ']')).click()
    # Click order button
    s('#calc_form > a').click()

@allure.step('Создание рандомного заказа с калькулятора, Type of paper  - Questions " ')
def random_calculate_question():
    s(by.xpath('.//select[@id="form_service_type"]/optgroup[5]/option[2]')).click()
    # Choice academic level
    b = str(random.randint(1, 3))
    s(by.xpath('.//select[@id="form_academic_level"]/option[' + b + ']')).click()
    # Choice deadline
    c = str(random.randint(1, 9))
    s(by.xpath('.//select[@id="form_deadline"]/option[' + c + ']')).click()
    # Choice number of pages
    d = str(random.randint(1, 10))
    s(by.xpath('.//select[@id="form_pages"]/option[' + d + ']')).click()
    # Click order button
    s('#calc_form > a').click()

#####Choice random type of service "Editing/proofreading" , "Typing" , "Other"
def random_calculate_other():
    b = str(random.randint(1, 3))
    s(by.xpath('.//*[@id="form_service_type"]/option[' + b + ']')).click()
    # Choice deadline
    c = str(random.randint(1, 9))
    s(by.xpath('.//select[@id="form_deadline"]/option[' + c + ']')).click()
    # Choice number of pages
    d = str(random.randint(1, 10))
    s(by.xpath('.//select[@id="form_pages"]/option[' + c + ']')).click()
    # Click order button
    s('#calc_form > a').click()

#####Choice random type of service "Typing" "
def random_calculate_other_typing():
    s(by.xpath('.//*[@id="form_service_type"]/option[2]')).click()
    # Choice deadline
    c = str(random.randint(1, 9))
    s(by.xpath('.//select[@id="form_deadline"]/option[' + c + ']')).click()
    # Choice number of pages
    d = str(random.randint(1, 10))
    s(by.xpath('.//select[@id="form_pages"]/option[' + c + ']')).click()
    # Click order button
    s('#calc_form > a').click()
