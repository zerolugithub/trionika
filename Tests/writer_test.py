#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf8
import os
import shutil

from selene.api import *
from selene.browsers import BrowserName

#from Support import support_main
#from data import mail, pwd, topic, paper_details, writerLogin, writerPass, discount_99
config.browser_name = BrowserName.CHROME
config.hold_browser_open = True   # This options for a Chrome
config.desired_capabilities={}
config.timeout = 10


class TestOrder:

    def setup(self):
        dir = os.getcwd()
        files = os.listdir(dir)
        for file in files:
            fullname = os.path.join(dir, file)
            if file == '.cache':
                shutil.rmtree(fullname)

    def teardown(self):
        browser.close()

    '''
    def test_order_ph2(self):
        browser.open_url("https://www.paperhelp.org/")
        browser.driver().maximize_window()
        ph.proceed_to_order()
        order.sign_in(mail, pwd)
        ph.choice_subject_random()
        order.choice_paper_format()
        order.set_sources_random()
        order.set_topic(topic)
        order.set_paper_details(paper_details)
        order.click_go_to_step3()
        price = order.order_price()
        order.set_discount(discount_99)
        order.click_proceed_to_secure_payment()
        order.checking_price(price)
        ph.go_to_admin_after_order()
        all_site.admin_modal_windows()
        order_number = ph.get_last_number_order()
        admin.pay_store_credit()
        support_main.status_paid_case_publish(order_number)
        wb_main.writer_apply(order_number)
        support_main.confirm_writer(order_number)
        wb_main.confirm_order(order_number)
        wb_main.add_file_to_order()'''
