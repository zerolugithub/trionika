# coding: utf8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import string
import allure
import pytest
import selene
from selene.conditions import text
from selene.api import *
import time

from webdriver_manager import driver

from General_pages.order_steps import random_mail
from data import writerLogin, writerPass, paper_details

def writer_login():
    browser.open_url("http://www.writerbay.com/")
    s(by.text('Login')).click()
    s(by.xpath('//div[@class="element"]/input[@name="email"]')).set_value(writerLogin)
    s(by.xpath('//div[@class="element"]/input[@name="pass"]')).set_value(writerPass)
    s(by.text('Sign in')).click()

def writer_apply(order):
    browser.open_url("http://www.writerbay.com/")
    s(by.text('Login')).click()
    s(by.xpath('//div[@class="element"]/input[@name="email"]')).set_value(writerLogin)
    s(by.xpath('//div[@class="element"]/input[@name="pass"]')).set_value(writerPass)
    s(by.text('Sign in')).click()
    browser.open_url("http://admin.writerbay.com/orders_available?subcom=detailed&id=%s" % order)
    s('#_reason').set_value(paper_details)
    s('#_apply').click()
    time.sleep(3)

def confirm_order(order):
    browser.open_url("http://admin.writerbay.com/my_orders/")
    s(by.text(order)).click()
    s('#confirmButton').click()

def add_file_to_order():
    time.sleep(3)
    s('.btn.btn-primary.btn-extra').click()
    time.sleep(3)
    s('.switch-file-form').click()      # switch to "Standart upload process"
    #s(by.xpath('.//*[@id="_upload_file"]/fieldset/div[5]/div/input')).clear()
    time.sleep(3)
    element = s(by.text("Upload new file"))
    browser.driver().execute_script("arguments[0].click();", element)
    s(by.text("Upload new file")).click()
    s(by.text("Upload new file")).set_value(os.getcwd() + "/Test.docx")
    #if s('#isFinal').is_displayed():
    #    s('#isFinal').click()
    #else:
    #    pass
    #s('[name="type"]').click()
    s(by.xpath('.//*[@id="_upload_file"]/fieldset/div[1]/select/option[3]')).click()
    time.sleep(5)
    s(by.xpath('//form[@id="_upload_file"]/fieldset/a/i')).click()
    s(by.xpath('.//*[@id="_upload_file"]/fieldset/div[4]/textarea')).set_value('test test test ')
    time.sleep(2)
    #s('input[type="file"]').click()
    #s(by.xpath('//div[@class="file-upload"]')).click()
    time.sleep(15)
    fileInput = s('//input[@type="file"]')
    time.sleep(10)
    fileInput.set_value(os.getcwd() + "/Test.docx")
    s('.btn.btn-primary._upload-file').click()
    time.sleep(10)
    '''
    +"arguments[0].style.opacity=1;"
        +"arguments[0].style['transform']='translate(0px, 0px) scale(1)';"
        +"arguments[0].style['MozTransform']='translate(0px, 0px) scale(1)';"
        +"arguments[0].style['WebkitTransform']='translate(0px, 0px) scale(1)';"
        +"arguments[0].style['msTransform']='translate(0px, 0px) scale(1)';"
        +"arguments[0].style['OTransform']='translate(0px, 0px) scale(1)';"
        +"return true"
    '''