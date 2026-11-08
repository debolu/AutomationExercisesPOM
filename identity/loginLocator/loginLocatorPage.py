from selenium.webdriver.common.by import By


class LoginActionLocator:
    # USERNAME = (By.ID, "user-name")
    # PASSWORD = (By.ID, "password")
    # LOGIN = (By.ID, "login-button")
    HOME_NAV_LINK = (By.XPATH, "//a[normalize-space()='Home']")
    SIGNUP_LOGIN = (By.XPATH, "//a[normalize-space()='Signup / Login']")
    NEW_SIGNUP_TEXT = (By.XPATH, "//h2[normalize-space()='New User Signup!']")
    NAME = (By.XPATH, "//input[@placeholder='Name']")
    EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP = (By.XPATH, "//button[normalize-space()='Signup']")
    ENTER_ACCOUNT_INFORMATION = (By.XPATH, "//b[normalize-space()='Enter Account Information']")

