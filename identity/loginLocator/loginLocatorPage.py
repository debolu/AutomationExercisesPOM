from selenium.webdriver.common.by import By


class LoginActionLocator:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")
    HOME_NAV_LINK = (By.XPATH, "//a[normalize-space()='Home']")

