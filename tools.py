import os
import subprocess
import signal
from selene import browser
from selene import config
from selene.browsers import BrowserName
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def scrollDown():
    browser.driver().execute_script(("window.scrollTo(0, document.body.scrollHeight);"))

#tearDownClass for phantomjs driver - close process
def tearDownClass(cls):
    """Tear down class."""
    try:
        cls.driver.quit()
        phantom_js_clean_up()
    except Exception as err:
        print(err)

def phantom_js_clean_up():
    """Clean up Phantom JS.

    Kills all phantomjs instances, disregard of their origin.
    """
    processes = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = processes.communicate()

    for line in out.splitlines():
        if 'phantomjs' in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)

def chrome_clean_up():
    """Clean up Phantom JS.

    Kills all phantomjs instances, disregard of their origin.
    """
    processes = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = processes.communicate()

    for line in out.splitlines():
        if 'chrome' or "chromedriver" in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)


class config_browser():

    def chrome_headless(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--window-size=1920,1080")
        #driver = webdriver.Chrome(executable_path='/Users/user/Desktop/chromedriver', chrome_options=chrome_options)
        driver = webdriver.Chrome(executable_path='/var/lib/jenkins/.wdm/chromedriver/2.34/chromedriver', chrome_options=chrome_options)    #### <----- Path to chomedriver on server
        browser.set_driver(driver)


    def phantomJS(self):
        config.browser_name = BrowserName.PHANTOMJS
        config.desired_capabilities = {}