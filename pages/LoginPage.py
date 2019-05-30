from pages.LoginLocators import LoginPageLocators


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def close_banner(self):
        self.driver.find_element(*LoginPageLocators.AGREE_BANNER_BUTTON).click()

    def click_login(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()