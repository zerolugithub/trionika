#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf8

import allure
from Tests import *
from selene.api import *

#Method to add screenshot to allure report
def pytest_exception_interact(node, call, report):
    driver = node.instance.driver
    allure.attach(
        name='Скриншот',
        body=browser.driver().get_screenshot_as_png(),
        attachment_type=allure.attachment_type.PNG,
    )


