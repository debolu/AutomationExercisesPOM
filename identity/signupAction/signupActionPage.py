import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.by import By

from config import config
from config.config import Config
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

    def choose_title(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.GENDER_MALE)
        )
        element.click()

    def enter_password(self, password):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.PASSWORD)
        )
        element.send_keys(password)

    def enter_dob(self, dob):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.DOB_DAY)
        )
        element.send_keys(dob[0]["day"])

        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.DOB_MONTH)
        )
        element.send_keys(dob[0]["month"])

        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.DOB_YEAR)
        )
        element.send_keys(dob[0]["year"])

    def accept_newsletter(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.NEWSLETTER_RADIO_BUTTON)
        )
        element.click()

    def accept_offer(self):
        # element =
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(SignupActionLocator.OFFERS_RADIO_BUTTON)
        ).click()

    def enter_first_name(self, first_name):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.FIRST_NAME)
        )
        element.send_keys(first_name)

    def enter_last_name(self, last_name):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.LAST_NAME)
        )
        element.send_keys(last_name)

    def enter_company_name (self, company):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.COMPANY_NAME)
        )
        element.send_keys(company)

    def enter_address (self, address, address_2):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.ADDRESS1)
        )
        element.send_keys(address)

        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.ADDRESS2)
        )
        element.send_keys(address_2)

    def enter_country(self, country):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.COUNTRY)
        )
        element.send_keys(country)

    def enter_state(self, state):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.STATE)
        )
        element.send_keys(state)

    def enter_city(self, city):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.CITY)
        )
        element.send_keys(city)

    def enter_zipcode(self, zipcode):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.ZIPCODE)
        )
        element.send_keys(zipcode)

    def enter_phone_number(self, phone_number):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.MOBILE_NUMBER)
        )
        element.send_keys(phone_number)

    def create_account_btn(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.CREATE_ACCOUNT)
        )
        element.click()

    def assert_account_created(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.ACCOUNT_CREATED_TEXT)
        )
        assert element.is_displayed()

    def click_continue_btn(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.CONTINUE_BTN)
        )
        element.click()

    def assert_logged_in_as_signup_name_text(self, name):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.LOGGED_IN_AS_FIRSTNAME_TEXT)
        )

        expected_text = f" Logged in as {name}"
        assert element.text == expected_text

    def delete_account (self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.DELETE_ACCOUNT)
        )
        element.click()

    def assert_account_deleted(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.ACCOUNT_DELETED_TEXT)
        )
        assert element.is_displayed()

        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(SignupActionLocator.CONTINUE_BTN)
        )
        element.click()


        time.sleep(5)














    # Test login flow
    # def enter_username(self, username):
    #     element = WebDriverWait(self.driver, 10).until(
    #         ec.presence_of_element_located(LoginActionLocator.USERNAME)
    #     )
    #     element.send_keys(username)
    #
    # def enter_password(self, password):
    #    element = WebDriverWait(self.driver, 10).until(
    #         ec.presence_of_element_located(LoginActionLocator.PASSWORD)
    #     )
    #     element.send_keys(password)
    #
    # def login(self):
    #     element = WebDriverWait(self.driver, 10).until(
    #         ec.presence_of_element_located(LoginActionLocator.LOGIN)
    #     )
    #     element.click()




