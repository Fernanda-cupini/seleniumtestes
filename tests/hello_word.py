import os
import unittest
import time
from selenium import webdriver
from pages.LoginPage import LoginPage


class NewTest(unittest.TestCase):
    """Testando um teste chato"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.implicitly_wait(5)
        self.base_url = "https://teamshift-qa.crossknowledge.com"
        self.driver.get(self.base_url)
        self.verificationErrors = []
        self.accept_next_alert = True

    def testFacebook(self):
        login = LoginPage(self.driver)
        login.close_banner()
        login.click_login()
        assert 'TeamSHIFT' in 'TeamSHIFT'

    def tearDown(self):
        self.driver.close()