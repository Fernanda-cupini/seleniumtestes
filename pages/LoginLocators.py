from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    AGREE_BANNER_BUTTON = (By.CSS_SELECTOR, 'div#js-cookie-policy[style="display: flex;"] button[id="js-agree-cookie-policy"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'body > main > header > nav > div.visible-lg-block > div > div > button')