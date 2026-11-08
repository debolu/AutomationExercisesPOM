import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.config import Config
from identity.signupAction.signupActionPage import SignupActionPage


# from identity.LoginAction.loginPage import LoginPage

@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()


# Launch the page using the URL.
@pytest.fixture(scope="function")
def signup(driver_setup):
    driver = driver_setup
    signup_page = SignupActionPage(driver)
    signup_page.open_signup_url(Config.BASE_URL)
    return signup_page

# Assert that the home page loads
def test_home_page_loads(signup):
    signup.assert_home_page_loads()

def test_signup(signup):
    signup.click_signup_login()
    signup.assert_new_signup_text()
    signup.enter_name(Config.SIGNUP_NAME)
    signup.enter_email(Config.SIGNUP_EMAIL)
    signup.signup()
    signup.assert_enter_account_information_text()
    signup.choose_title()
    signup.enter_password(Config.PASSWORD)
    signup.enter_dob(Config.DOB)
    signup.accept_newsletter()
    signup.accept_offer()
    signup.enter_first_name(Config.SIGNUP_NAME)
    signup.enter_last_name(Config.LAST_NAME)
    signup.enter_company_name(Config.COMPANY)
    signup.enter_address(Config.ADDRESS, Config.ADDRESS_2)
    signup.enter_country(Config.COUNTRY)
    signup.enter_state(Config.STATE)
    signup.enter_city(Config.CITY)
    signup.enter_zipcode(Config.ZIPCODE)
    signup.enter_phone_number(Config.MOBILE_NUMBER)
    signup.create_account_btn()
    signup.assert_account_created()
    signup.click_continue_btn()
    signup.assert_logged_in_as_signup_name_text(Config.SIGNUP_NAME)
    signup.delete_account()
    signup.assert_account_deleted()
    signup.click_continue_btn()








# Login using the username and the password.
# def test_login(login):
#     login.enter_username("standard_user")
#     login.enter_password("secret_sauce")
#     login.login()



