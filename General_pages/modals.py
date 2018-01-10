# coding: utf8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from selene.browser import open_url, driver
from selene.support import by
from selene.support.conditions.be import visible
from selene.api import *
from selene import browser
import time

@allure.step("Закрытие модального окна авторизации в админке клиента")
def modal_admin_auth_close():
    time.sleep(3)
    if s(by.xpath(".//div[@id='verification_modal']/div")).assure(visible):
        s('#verification_remind').click()   # click on checkpython box "Never remind me again"
        s(by.xpath('.//*[@id="verification_modal"]/div/div/div[1]/button')).click()
    else:
        print 'Modal window not visible'

@allure.step("Закрытие модального окна реферал в админке клиента")
def modal_admin_referral_close():
    if s('.close-btn').is_displayed():
        s('.close-btn').click()
    else:
        print 'Modal window not visible'

@allure.step("Закрытие модального окна реферал в админке клиента")
def modal_upgrade_order():
    time.sleep(2)
    if s('#last-step-order-form-modal > div > div > div.text_help.text2_modal > div.modal-footer > a').is_displayed():
        s('#last-step-order-form-modal > div > div > div.text_help.text2_modal > div.modal-footer > a').click()
    else:
        print 'Modal window not visible'
        #s('#last-step-order-form-modal > div > div > div.text_help.text2_modal > div.modal-footer > a').click()


def modal_admin_unpaid_order():
    if s('#no_have_upaid_order_modal_cross').is_displayed():
        s('#no_have_upaid_order_modal_cross').click()
    else:
        print 'Modal window not visible'


