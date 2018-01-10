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

#--------------------  PH
from selenium.common.exceptions import TimeoutException


def close_modal_start_window():
    time.sleep(3)
    if s('.close').is_displayed():
        s('.close').click()
    else:
        pass
@allure.step('Закрытие модалього окна "Upgrade now!" перед переходом на страницу платежной системы')
def close_modal_upgrade_now():
    time.sleep(2)
    if s(by.text('No, continue with my original order')):             #s(by.xpath('//div[@id="last-step-order-form-modal"]/div')).is_displayed():
        if s(by.xpath('//div[@class="modal-footer"]/a[@class="go_to_proc ab1_test_nothx"]')).is_displayed():
            s(by.xpath('//div[@class="modal-footer"]/a[@class="go_to_proc ab1_test_nothx"]')).click()
        elif s(by.xpath('//div[@class="modal-footer"]/a[@class="go_to_proc ab2_test_nothx"]')).is_displayed():
            s(by.xpath('//div[@class="modal-footer"]/a[@class="go_to_proc ab2_test_nothx"]')).click()
        elif s(by.xpath('//div[@class="modal-footer"]/a[@class="go_to_proc ab3_test_nothx"]')).is_displayed():
            s(by.xpath('//div[@class="modal-footer"]/a[@class="go_to_proc ab3_test_nothx"]')).click()
    else:
        pass

@allure.step('Закрытие модалього окна "Authorization" в админке клиента')
def close_Authorization_window():
    try:
        if s(by.xpath('//div[@id="verification_modal"]/div')).is_displayed():
            s(by.xpath('.//*[@id="verification_modal"]/div/div/div[1]/button')).click().press_enter()
    except TimeoutException:
        return True
    #if s('.introjs-button.introjs-skipbutton').is_displayed():
    #    s('.introjs-button.introjs-skipbutton').click()
    #else:
    #    pass
@allure.step('Закрытие модалього окна ')
def admin_modal_windows():
    if s(by.xpath('.//*[@id="verification_modal"]/div/div/div[1]/button')).is_displayed():
        s(by.xpath('.//*[@id="verification_modal"]/div/div/div[1]/button')).click()


def scroll_down():
    browser.driver().execute_script(("window.scrollTo(0, document.body.scrollHeight);"))

def click_done():
    s(by.text('Done')).click()