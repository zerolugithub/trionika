# coding: utf8
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from selene.support import by
from selene.api import *
from selene import browser
import time


def new_order(self):
    time.sleep(1)
    s('#header > div > div.col-xs-10 > a.btn.btn-new-order.btn-primary.btn-lg').click()

def pay_store_credit():
    s('.btn.btn-pay.btn-primary.statistic_send').click()
    time.sleep(1)
    s('._show_pay_with_credit_form.btn.btn-default.btn-block').click()   # choice Store Credit
    time.sleep(1)
    s('.btn.btn-primary._submit_pay_with_credit_form').click()           # Pay Store Credit
    time.sleep(3)