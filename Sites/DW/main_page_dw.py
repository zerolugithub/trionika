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

from General_pages.order_steps import random_mail

# Type of paper  - Essays, Homework Help, Dissertation , Admissions
def choice_type_of_paper_essays():
    a = str(random.randint(1, 3))
    if a == '2':
        print 'Сategory  - Essays'
        count = str(random.randint(1, 24))
    elif a == '1':
        print 'Сategory  - Dissertation'
        print  'Academic level change to Professional'
        count = str(random.randint(1, 10))
    elif a == '3':
        print 'Сategory  - Homework Help'
        count = str(random.randint(1, 8))
    else:
        count = str(random.randint(1, 6))
    type_of_paper = s(by.xpath('.//select[@id="type_of_paper"]/optgroup[' + a + ']/option[' + count + ']')).text
    s(by.xpath('.//select[@id="type_of_paper"]/optgroup[' + a + ']/option[' + count + ']')).click()
    print 'Type of paper is ' + type_of_paper

@allure.step("Нажимаем на кнопку Sign In")
def click_sign_in():
    s('.h_login_button').click()


    # page_wrap > header > div.clien_area > a
# # Type of paper  - Questions
# def choice_type_of_paper_Questions():
#     type_of_paper = s(by.xpath('.//select[@id="type_of_paper"]/optgroup[4]/option[1]')).text
#     s(by.xpath('.//select[@id="type_of_paper"]/optgroup[4]/option[1]')).click()
#     print 'Type of paper is ' + type_of_paper
#
# # Type of paper  - Problems
# def choice_type_of_paper_Problems():
#     type_of_paper = s(by.xpath('.//select[@id="type_of_paper"]/optgroup[4]/option[2]')).text
#     s(by.xpath('.//select[@id="type_of_paper"]/optgroup[4]/option[2]')).click()
#     print 'Type of paper is ' + type_of_paper
#
# # Type of paper  - Admission
# def choice_type_of_paper_Admission():
#     a = str(random.randint(1, 6))
#     type_of_paper = s(by.xpath('.//select[@id="type_of_paper"]/optgroup[5]/option[' + a + ']')).text
#     s(by.xpath('.//select[@id="type_of_paper"]/optgroup[5]/option[' + a + ']')).click()
#     print 'Type of paper is ' + type_of_paper
#
# # Type of paper  - Other
# def choice_type_of_paper_other():
#     a = str(random.randint(1, 3))
#     type_of_paper = s(by.xpath('.//select[@id="type_of_paper"]/option[' + a + ']')).text
#     s(by.xpath('.//select[@id="type_of_paper"]/option[' + a + ']')).click()
#     print 'Type of paper is ' + type_of_paper