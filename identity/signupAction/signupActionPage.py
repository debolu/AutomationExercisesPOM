import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.by import By

from identity.signupLocator.signupLocatorPage import SignupActionLocator


class SignupActionPage:

    def __init__(self, driver):
        self.driver = driver

    def open_signup_url(self, url):
        self.driver.get(url)

    def assert_home_page_loads(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.HOME_NAV_LINK)
        )
        assert element.is_displayed()

    def click_signup_login(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.SIGNUP_LOGIN)
        )
        element.click()

    # assert new user signup text is present.
    def assert_new_signup_text(self):
        print(self.driver.current_url)
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.NEW_SIGNUP_TEXT)
        )
        print("Text found:", element.text)
        print("Displayed:", element.is_displayed())
        assert element.is_displayed()

    def enter_name(self, name):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.NAME)
        )
        element.send_keys(name)

    def enter_email(self, email):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.EMAIL)
        )
        element.send_keys(email)

    def signup(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.SIGNUP)
        )
        element.click()

    def assert_enter_account_information_text(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.ENTER_ACCOUNT_INFORMATION)
        )
        assert element.is_displayed()


    # Test login flow
    # def enter_username(self, username):
    #     element = WebDriverWait(self.driver, 10).until(
    #         ec.presence_of_element_located(LoginActionLocator.USERNAME)
    #     )
    #     element.send_keys(username)
    #
    # def enter_password(self, password):
    #     element = WebDriverWait(self.driver, 10).until(
    #         ec.presence_of_element_located(LoginActionLocator.PASSWORD)
    #     )
    #     element.send_keys(password)
    #
    # def login(self):
    #     element = WebDriverWait(self.driver, 10).until(
    #         ec.presence_of_element_located(LoginActionLocator.LOGIN)
    #     )
    #     element.click()
        time.sleep(5)


