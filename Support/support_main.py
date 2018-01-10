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
from data import writerLogin, writerPass, paper_details, supportLogin, supportPass


def status_paid_case_publish(order):
    browser.open_url("http://support.wenthost.org/auth/orders/")                            # Go to support site
    s('[name=email]').set_value(supportLogin)                                               # Set login
    s('[name=pass]').set_value(supportPass)                                                 # Set password
    s(by.text('Sign in')).click()                                                           # Click 'Sign In' button
    browser.open_url("http://support.wenthost.org/orders?subcom=detailed&id=%s" % order)    # go to current order page
    s(by.xpath('//a[@class="btn dropdown-toggle"]')).click()                                # Click on status drop down button
    s(by.xpath('//a[@status="8"]')).click()                                                 # Change status for Case Published
    time.sleep(2)
    s(by.xpath('.//*[@id="writer_link_setiings_form"]/div[2]/button[2]')).click()           # Submit choice
    time.sleep(2)


def confirm_writer(order):
    browser.open_url("http://support.wenthost.org/orders?subcom=detailed&id=%s" % order)
    s('#inside-block-writer-appl-button').click()
    time.sleep(1)
    s('.btn.btn-small.btn-green._confirm_writer_apply').click()
    time.sleep(5)


