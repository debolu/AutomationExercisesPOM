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



@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginActionPage(driver)
    login_page.open_login_url("https://www.saucedemo.com")
    return login_page

def test_login(login):
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.login()
