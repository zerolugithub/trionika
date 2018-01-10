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

from selenium.common.exceptions import TimeoutException

from General_pages.order_steps import random_mail

@allure.step('Выбираем случайны  Subject')
def choice_subject_random():
    n = str(random.randint(2, 20))
    #time.sleep(1)
    #s(by.xpath('.//*[@id="select2"]')).click()
    time.sleep(1)
    subject = s(by.xpath('.//*[@id="select2"]/optgroup/option[' + n + ']')).text
    s(by.xpath('.//*[@id="select2"]/optgroup/option[' + n + ']')).click()
    print 'Order subject is ' + subject

# Type of paper  - Essays, Homework Help, Dissertation , Admissions
@allure.step('Случайный выбор Type of paper  - Essays, Homework Help, Dissertation , Admissions')
def choice_type_of_paper_essays():
    a = str(random.randint(1, 3))
    if a == '1':
        print 'Сategory  - Essays'
        count = str(random.randint(1, 24))
    elif a == '2':
        print 'Сategory  - Dissertation'
        print  'Academic level change to Professional'
        count = str(random.randint(1, 9))
    elif a == '3':
        print 'Сategory  - Homework Help'
        count = str(random.randint(1, 8))
    else:
        count = str(random.randint(1, 6))
    type_of_paper = s(by.xpath('.//select[@name="type_of_paper"]/optgroup[' + a + ']/option[' + count + ']')).text
    s(by.xpath('.//select[@id="type_of_paper"]/optgroup[' + a + ']/option[' + count + ']')).click()
    print 'Type of paper is ' + type_of_paper

@allure.step('Заполняем поле Topic - Test')
def set_topic(topic):
    s('#topic').set_value(topic)

@allure.step('Заполняем поле Paper Details: - IT Test Autamation ')
def set_paper_details(paper_details):
    s('#instructions').set_value(paper_details)

@allure.step('Выбираем  Paper Format')
def choice_paper_format():
    n = str(random.randint(2, 5))
    s(by.xpath('//select[@id="select4"]/option[' + n + ']')).click()

@allure.step(' Нажать на кнопку "Proceed to payment"')
def click_proceed_to_secure_payment():
    time.sleep(2)
    s('#create_order').click()


@allure.step('Генерируем случайное число и вводим в поле Number of slides')
def set_number_of_slides():
    n = random.randint(1, 10)
    s('._slides.form-input').set_value(n)

def regigister():
    time.sleep(1)
    s('#ui-id-1').click()
    s('#name').set_value('Test')
    s('#surname').set_value('test')
    s('#email1').set_value(random_mail())
    s('#password1').set_value('123123')
    s('[name="phone_number"]').set_value('123123123')

@allure.step('Заполнение формы для регистрации старого пользователя')
def login_on_order_page(email, pwd):
    time.sleep(1)
    s('#ui-id-2').click()
    s('#email').set_value(email)
    s('#password').set_value(pwd)

@allure.step('Запоминаем значение поля TOTAL PRICE')
def order_price():
    time.sleep(2)
    price = s('#appr_price').text
    price = price[1:]
    return price

def choice_academic_level():
    n = random.randint(0, 2)
    academic_level_list = ['Undergraduate','Master','Ph.D.']
    academic_level = academic_level_list[n]
    print 'Academic level is ' + academic_level.upper()
    s(by.text('%s'%academic_level)).click()

# Type of paper  - Essays, Homework Help, Dissertation , Admissions
def choice_type_of_paper_essays():
    a = str(random.randint(1, 3))
    if a == '1':
        print 'Сategory  - Essays'
        count = str(random.randint(1, 24))
    elif a == '2':
        print 'Сategory  - Dissertation'
        print  'Academic level change to Professional'
        count = str(random.randint(1, 9))
    elif a == '3':
        print 'Сategory  - Homework Help'
        count = str(random.randint(1, 8))
    else:
        count = str(random.randint(1, 6))
    type_of_paper = s(by.xpath('.//*[@id="select1"]/optgroup[' + a + ']/option[' + count + ']')).text
    s(by.xpath('.//*[@id="select1"]/optgroup[' + a + ']/option[' + count + ']')).click()
    print 'Type of paper is ' + type_of_paper

# Type of paper  - Questions
def choice_type_of_paper_Questions():
    type_of_paper = s(by.xpath('.//*[@id="select1"]/optgroup[4]/option[1]')).text
    s(by.xpath('.//*[@id="select1"]/optgroup[4]/option[1]')).click()
    print 'Type of paper is ' + type_of_paper

# Type of paper  - Problems
def choice_type_of_paper_Problems():
    type_of_paper = s(by.xpath('.//*[@id="select1"]/optgroup[4]/option[2]')).text
    s(by.xpath('.//*[@id="select1"]/optgroup[4]/option[2]')).click()
    print 'Type of paper is ' + type_of_paper

# Type of paper  - Admission
def choice_type_of_paper_Admission():
    a = str(random.randint(1, 6))
    type_of_paper = s(by.xpath('.//*[@id="select1"]/optgroup[5]/option[' + a + ']')).text
    s(by.xpath('.//*[@id="select1"]/optgroup[5]/option[' + a + ']')).click()
    print 'Type of paper is ' + type_of_paper


def set_single_or_double_spaced():
    if s(by.xpath('//div[@class="btn-group btn-group-justified"]')).is_displayed():
        n = random.randint(1, 2)
        n=str(n)
        s(by.xpath('//div[@class="btn-group btn-group-justified"]/label[' + n + ']')).click()
        if n=='1':
            print 'Order has Single Spaced'
        if n=='2':
            print 'Order has Double Spaced'
    else:
        print 'Type of paper is Homework Help, and don\'t has option single or double space'

@allure.step('Случайный выбор Subject')
def choice_subject_random(subject_list):
    n = str(random.randint(2, 20))
    time.sleep(1)
    s('#select2').click()
    time.sleep(1)
    s(by.xpath('//select[@class="form-control custom-select"]/optgroup[@label="Arts & Humanities"]/option[' + n + ']')).click()
    n=int(n)
    subject = subject_list[n]
    print 'Order subject is ' + subject

@allure.step('Генерируем случайное число и вводим в поле Number of slides')
def set_number_of_slides():      # 30% that this option will be selected
    Chance_to_use= random.randint(1, 10)
    if Chance_to_use in [1,2,3]:
        n = random.randint(1, 15)
        s('[name="slides"]').set_value(n)
        n = str(n)
        print 'Count of slides is ' + n
    else:
        pass

@allure.step('Генерируем случайное число и вводим в поле Number of slides')
def set_number_of_pages():      # 30% that this option will be selected
    Chance_to_use= random.randint(1, 10)
    if Chance_to_use in [1,2,3]:
        n = random.randint(1, 15)
        s('[name="pages"]').set_value(n)
        n = str(n)
        print 'Count of pages is ' + n

    else:
        pass
    while True:
        try:
            alert = s('error="pages"').text
        except TimeoutException:
            return True
    else:
        if s('error="pages"').is_displayed():
            error = s('error="pages"').text
            print error
            count = error.split(' ')[-9]
            count = int(count)
            s('[name="pages"]').set_value(count)
            count = str(count)
            print 'Count of pages change to ' + count + ' because deadline it does not allow more'


def choice_additional_materials(addition_materials_list):
    n = random.randint(1, 3)
    time.sleep(1)
    n =str(n)
    s('#select3').click()
    #print addition_materials_list[n]
    s(by.xpath('.//*[@id="select3"]/option[' + n + ']')).click()
    m = random.randint(0, 2)
    print 'Additional Materials: ' + addition_materials_list[m]

def choice_paper_format_random_step_inquiry():
    time.sleep(1)
    n = str(random.randint(2, 6))
    s('#select4').click()
    s(by.xpath('.//*[@id="select4"]/option[' + n + ']')).click()
    paper_format_dict = { 2 : 'MLA', 3 : 'APA', 4 : 'Chicago/ Turabian', 5 : 'Harvard', 6 : 'Other'}
    n=int(n)
    print 'Paper format is ' + paper_format_dict[n]

def choice_deadline():
    n = str(random.randint(1, 9))
    deadline = s(by.xpath('//div[@class="btn-group btn-group-justified deadline-block"]/label[' + n + ']')).text
    s(by.xpath('//div[@class="btn-group btn-group-justified deadline-block"]/label[' + n + ']')).click()
    print 'Deadline on this order ' + deadline

def choice_payment_system():   # Choice Credit card or PayPal
    n = str(random.randint(1, 2))
    s(by.xpath('//div[@class="btn-group btn-group-justified radio-group"]/div[' + n + ']')).click()

@allure.step(' Нажать на кнопку "Proceed to secure payment" при создании inquiry')
def click_proceed_to_secure_payment_inquiry():
    time.sleep(2)
    price = s('#appr_price').text
    price = price[1:]
    #s('#payment_button_admin').submit()
    s('#create_order').double_click()
    return price