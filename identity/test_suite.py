import pytest
from selenium import webdriver
# from config.config import Config
from selenium.webdriver.chrome.options import Options

from identity.loginAction.loginActionPage import LoginActionPage


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
def login(driver_setup):
    driver = driver_setup
    login_page = LoginActionPage(driver)
    login_page.open_login_url("https://automationexercise.com/")
    return login_page

# Assert that the home page loads
def test_home_page_loads(login):
    login.assert_home_page_loads()

def test_signup(login):
    login.click_signup_login()
    login.assert_new_signup_text()
    login.enter_name("Adebolu")
    login.enter_email("tantether@tiffincrane.com")
    login.signup()
    login.assert_enter_account_information_text()




# Login using the username and the password.
# def test_login(login):
#     login.enter_username("standard_user")
#     login.enter_password("secret_sauce")
#     login.login()



