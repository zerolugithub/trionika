# coding: utf8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string
import allure
import pytest
from selene import driver
from selene import tools
from selene.conditions import text, visible
from selene.api import *
import time

from selenium.common.exceptions import TimeoutException

from General_pages.order_steps import random_mail
from data import discount_error, discount, subject_list
from selenium import webdriver
from loremipsum import generate_paragraph
from tools import scrollDown


@allure.step("Вводим мейл и пароль, нажимаем кнопку Submit ")
def set_mail_and_pass(mail, pwd):
    s('#inputEmail3').set_value(mail)
    s('#inputPassword3').set_value(pwd)
    s('.btn.btn-default.btn-block.btn-login').click()

@allure.step("Нажать на кнопку NEW ORDER в админке клиента ")
def click_create_order_button_admin():
    # time.sleep(1)
    # if s(by.xpath(".//div[@id='verification_modal']/div")).assure(visible):
    #     s('#verification_remind').click()   # click on checkpython box "Never remind me again"
    #     s(by.xpath('.//*[@id="verification_modal"]/div/div/div[1]/button')).click()
    # else:
    #     print 'Modal window not visible'
    time.sleep(10)
    s(by.xpath('//a[@href="/order"][2]')).click()

@allure.step("Нажать на кнопку NEW ORDER в админке клиента ")
def click_create_order_button_admin_text():
    time.sleep(10)
    s(by.xpath('//div[@class="table-cell"]/a[@href="/order"]')).click()

@allure.step('Случайный выбор Academic Level')
def choice_academic_level():
    time.sleep(2)
    n = random.randint(0, 2)
    academic_level_list = ['undergraduate','master','professional']
    academic_level = academic_level_list[n]
    print 'Academic level is ' + academic_level.upper()
    if s('#%s'%academic_level).is_displayed():
        s('#%s' % academic_level).click().click()
    else:
        pass

# Type of paper  - Essays, Homework Help, Dissertation , Admissions
@allure.step('Случайный выбор Type of paper  - Essays, Homework Help, Dissertation , Admissions')
def choice_type_of_paper_essays():
    a = str(random.randint(1, 3))
    if a == '1':
        print 'Category  - Essays'
        count = str(random.randint(1, 24))
    elif a == '2':
        print 'Category  - Dissertation'
        print  'Academic level change to Professional'
        count = str(random.randint(1, 9))
    elif a == '3':
        print 'Category  - Homework Help'
        count = str(random.randint(1, 8))
    else:
        count = str(random.randint(1, 6))
    type_of_paper = s(by.xpath('.//select[@id="type_of_paper"]/optgroup[' + a + ']/option[' + count + ']')).text
    s(by.xpath('.//select[@id="type_of_paper"]/optgroup[' + a + ']/option[' + count + ']')).click()
    print 'Type of paper is ' + type_of_paper

# Type of paper  - Questions
@allure.step('Случайный выбор Type of paper  - Questions')
def choice_type_of_paper_Questions():
    type_of_paper = s(by.xpath('.//select[@id="type_of_paper"]/optgroup[4]/option[1]')).text
    s(by.xpath('.//select[@id="type_of_paper"]/optgroup[4]/option[1]')).click()
    print 'Type of paper is ' + type_of_paper

# Type of paper  - Problems
@allure.step('Случайный выбор Type of paper  - Problems')
def choice_type_of_paper_Problems():
    type_of_paper = s(by.xpath('.//select[@id="type_of_paper"]/optgroup[4]/option[2]')).text
    s(by.xpath('.//select[@id="type_of_paper"]/optgroup[4]/option[2]')).click()
    print 'Type of paper is ' + type_of_paper

# Type of paper  - Admission
@allure.step('Случайный выбор Type of paper  - Admission')
def choice_type_of_paper_Admission():
    a = str(random.randint(1, 6))
    type_of_paper = s(by.xpath('.//select[@id="type_of_paper"]/optgroup[5]/option[' + a + ']')).text
    s(by.xpath('.//select[@id="type_of_paper"]/optgroup[5]/option[' + a + ']')).click()
    print 'Type of paper is ' + type_of_paper

# Type of paper  - Other
@allure.step('Случайный выбор Type of paper  - Other')
def choice_type_of_paper_other():
    a = str(random.randint(1, 3))
    type_of_paper = s(by.xpath('.//select[@id="type_of_paper"]/option[' + a + ']')).text
    s(by.xpath('.//select[@id="type_of_paper"]/option[' + a + ']')).click()
    print 'Type of paper is ' + type_of_paper

#### Choice subject with subject list
@allure.step('Случайный выбор Subject')
def choice_subject_random(subject_list):
    n = str(random.randint(2, 69))
    time.sleep(3)
    s('#subject_test').click()
    s(by.xpath('//ul[@id="ui-id-1"]/li[' + n + ']')).click()
    n=int(n)
    subject = subject_list[n]
    print 'Order subject is ' + subject

#### Choice subject simple version
@allure.step('Выбираем случайны  Subject')    ####Must be new method to choice subject on admin page
def choice_subject_random():
    n = str(random.randint(2, 69))
    time.sleep(1)
    s('#subject_test').click()
    s(by.xpath('//ul[@id="ui-id-1"]/li[' + n + ']')).click()

@allure.step('Заполняем поле Topic - Test')
def set_topic(topic):
    s('[name="topic"]').set_value(topic)
    print 'Topic - ' + topic

@allure.step('Заполняем поле Paper Details: - случайным текстом lauren ipsum ')
def set_paper_details_LI():
    sentences_count, words_count, paragraph = generate_paragraph()
    text_paper_details=str(generate_paragraph())
    text = str(generate_paragraph())
    s('[name="paper_details"]').set_value(text)
    print 'Paper details - ' + text

@allure.step('Заполняем поле Paper Details: - IT Test Autamation ')
def set_paper_details(paper_details):
    s('[name="paper_details"]').set_value(paper_details)
    print 'Paper details - ' + paper_details

@allure.step('Случайный выбор Single or Double spaced')
def set_single_or_double_spaced():
    if s(by.xpath('//div[@class="button-group button-group-justified radio-group"]')).is_displayed():
        n = random.randint(1, 2)
        n=str(n)
        s(by.xpath('//div[@class="button-group button-group-justified radio-group"]/div[' + n + ']')).click()
        if n=='1':
            print 'Order has Single Spaced'
        if n=='2':
            print 'Order has Double Spaced'
    else:
        print 'Type of paper is Homework Help, and don\'t has option single or double space'

@allure.step('Генерируем случайное число и вводим в поле Number of Pages')
def set_number_of_pages_random():
    n = random.randint(1, 20)
    s('[name="pages"]').click()
    s('[name="pages"]').set_value(n).press_enter()
    n=str(n)
    print 'Count of pages is ' + n
    time.sleep(1)
    if s(by.xpath('//div[@class="block-6 help-empty-class block_element"]/div[2]')).is_displayed():
        alert = s(by.xpath('//div[@class="block-6 help-empty-class block_element"]/div[2]')).text
        count = alert.split(' ')[-9]
        s('[name="pages"]').set_value(count)
        print 'Count of pages change to ' + count + ' because deadline it does not allow more'
    else:
        pass


@allure.step('Генерируем случайное число и вводим в поле Number of slides')
def set_job_title_and_reasons_inquiry():
    time.sleep(4)
    if s('[name="institution"]').is_displayed():
        n = str(random.randint(2, 8))
        Type_of_institution = s(by.xpath('.//*[@id="_type_of_institution"]/div[2]/select/option[' + n + ']')).text
        s(by.xpath('.//*[@id="_type_of_institution"]/div[2]/select/option[' + n + ']')).click()
        s('[name="institution"]').set_value('AutoTest')
        print  "Type_of_institution is " + Type_of_institution
        print  "Institution is AutoTest"
    else:
        s('[name="reasons_for_applying"]').set_value('Test')
        print  "Reasons for applying is AutoTest"
        s('[name="job_title_or_industry"]').set_value('Test')
        print  "Job title or industry is AutoTest"

@allure.step('Случайный выбор Paper format')
def choice_paper_format_random_step_inquiry():
    if s('#_paper_format > div.col-sm-9 > div.btn-group.btn-group-justified.radio-group.order-desktop-view').is_displayed():
        n = str(random.randint(1, 5))
        s(by.xpath('//div[@class="btn-group btn-group-justified radio-group order-desktop-view"]/div[' + n + ']')).click()
        paper_format_dict = { 1 : 'MLA', 2 : 'APA', 3 : 'Chicago/ Turabian', 4 : 'Harvard', 5 : 'Other'}
        n=int(n)
        print 'Paper format is ' + paper_format_dict[n]
    else:
        print 'It is impossible to select Paper Format for this type of work'

@allure.step('Случайный выбор платежной системы')
def choice_payment_system():   # Choice Credit card or PayPal
    n = str(random.randint(1, 2))
    s(by.xpath('.//*[@id="_choose_pay_system"]/div[2]/div/div[' + n + ']/label')).click()
    time.sleep(3)


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

@allure.step('Генерируем случайное число и вводим в поле Sources')
def set_number_of_sources():      # 30% that this option will be selected
    Chance_to_use = random.randint(1, 10)
    if Chance_to_use in [1, 2, 3]:
        n = random.randint(1, 15)
        s('[name="sources_needed"]').set_value(n)
        n = str(n)
        print 'Count of sources is ' + n

@allure.step('Случайный выбор опции Additional Materials')
def choice_additional_materials(addition_materials_list):
    n = random.randint(0, 2)
    time.sleep(1)
    s(by.text(addition_materials_list[n])).click()
    print 'Additional Materials: ' + addition_materials_list[n]

@allure.step('Случайный выбор опции Preferred writer')
def choice_option_preferred_writer(preferred_writer_option_list,id):
    n = random.randint(0, 3)
    s(by.text(preferred_writer_option_list[n])).click()
    print 'Preferred writer: ' + preferred_writer_option_list[n]
    if n==2:                                                        # If choice option "My previous writer" set id writer
        if s('[name="previous_writer"]').is_displayed():
            s('[name="previous_writer"]').set_value(id)    #.press_enter()
            print 'Writer ID = 263529979'
        else:
            print '"My previous writer" can not be selected because of deadline very small for this options\n Preferred writer: Regular writer'

@allure.step('Случайный выбор опции  "I want to order VIP customer service"')
def choice_VIP_customer_sevice():  # 10% that this option will be selected
    n = random.randint(1, 10)
    s('[name="top_priority"]').double_click()
    if n==5:
        s('[name="top_priority"]').click()
        time.sleep(2)
        print "Check option \"I want to order VIP customer service\""
    else:
        pass

@allure.step('Случайный выбор опции  " I want to receive official Plagiarism report"')
def choice_Plagiarism_report():    # 10% that this option will be selected
    n = random.randint(1, 10)
    if n==5:
        s('[name="plagiarism_report"]').click()
        time.sleep(2)
        print "Check option \"I want to receive official Plagiarism report\""
    else:
        pass

@allure.step('Случайный выбор опции  "Add an Abstract page to my paper"')
def choice_Abstract_page():        # 10% that this option will be selected
    n = random.randint(1, 10)
    if n==5:
        s('[name="abstract_page"]').click()
        time.sleep(2)
        print "Check option \"Add an Abstract page to my paper\""
    else:
        pass

@allure.step('Устанавливаем рандомный Deadline')
def choice_deadline():
    n = random.randint(0, 8)
    deadline_list = ['1035', '1036', '1037', '1002', '1003','1004', '1007', '1011', '1015' ]
    deadline = deadline_list[n]
    s(by.xpath('//input[@name="deadline"][@value="%s"]/..'%deadline)).click()
    deadline_dict = { '1035':'3Hours', '1036':'6Hours', '1037':'12Hours', '1002':'24Hours', '1003':'2Days','1004':'3Days', '1007':'6Days', '1011':'10Days', '1015':'14Days' }
    print 'Deadline on this inquiry ' + deadline_dict[deadline]


@allure.step('Заполнение формы для регистрации нового пользователя')
def i_am_new():
    s('#order_contact_block > ul > li:nth-child(2) > a').click()
    s('[name="first_name"]').set_value('AutoTest')
    s('[name="last_name"]').set_value('test')
    s('[name="email"]').set_value(random_mail())
    s('[name="phone_number"]').set_value('123123123')
    time.sleep(1)

@allure.step('Заполнение формы для регистрации старого пользователя')
def sign_in(email, pwd):
    s('[name="email_reg"]').set_value(email)
    s('[name="password_reg"]').set_value(pwd)
    time.sleep(1)

@allure.step('Нажать на кнопку Submit Inquiry')
def click_submit_inquiry():
    time.sleep(1)
    scrollDown()
    s(by.text('Submit Inquiry')).double_click()
    print 'Click Submit Inquiry'


@allure.step('Генерируем случайное число и вводим в поле Problems ')
def set_problems_inquiry():
    time.sleep(2)
    n = random.randint(1, 25)
    s('[name="problems_inquiry"]').set_value(n)
    n =str(n)
    print 'Count of problems ' + n
    while True:
        try:
            alert = s(by.xpath('//div[@error="problems_inquiry"]')).text
        except TimeoutException:
            return True
        else:
            alert = s(by.xpath('//div[@error="problems_inquiry"]')).text
            count = alert.split(' ')[-1]
            count = count[0:-1]
            s('[name="problems_inquiry"]').set_value(count)
            print alert + '\nCount of problems change to ' + count + ', minimal for current deadline'
            break

@allure.step('Генерируем случайное число и вводим в поле Questions')
def set_questions():
    n = random.randint(1, 30)
    s('[name="questions_inquiry" ]').click()
    s('[name="questions_inquiry" ]').set_value(n)
    n = str(n)
    print 'Count of questions ' + n