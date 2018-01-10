import os

import allure
import time
from selene.api import *
from selene.browsers import BrowserName
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from tools import config_browser

config_browser().chrome_headless()

class Test_Spotify:
    driver = browser.driver()

    def setup(m):
        config_browser().chrome_headless()
        print '\n ****************** START TEST  ************** \n'

    def teardown(m):
        print '\n ****************** END TEST  ***************** \n'
        browser.driver().delete_all_cookies()
        browser.close()

    def test_login_spotify_vadim(self):
        browser.open_url("https://www.spotify.com/us/")
        s('#header-login-link > span').click()
        s('#login-username').send_keys('shoposhapkam@gmail.com')
        s('#login-password').send_keys('qwer12')
        s('body > div.container-fluid.login.ng-scope > div > form > div.row.row-submit > div:nth-child(2) > button').click()
        time.sleep(3)
        print browser.driver().title
        s('#card-profile-username').should(have.text('xthybz6t776xyu5xmm1hdxb2j'))


    def test_login_spotify_staf(self):
        browser.open_url("https://www.spotify.com/us/")
        s('#header-login-link > span').click()
        s('#login-username').send_keys('staf26')
        s('#login-password').send_keys('111111')
        s('body > div.container-fluid.login.ng-scope > div > form > div.row.row-submit > div:nth-child(2) > button').click()
        time.sleep(3)
        print browser.driver().title
        s('#card-profile-username').should(have.text('staf26'))