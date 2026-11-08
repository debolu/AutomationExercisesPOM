from selenium.webdriver.common.by import By


class SignupActionLocator:
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
    GENDER_MALE = (By.ID, "id_gender1")
    GENDER_FEMALE = (By.ID, "id_gender2")
    PASSWORD = (By.ID, "password")
    DOB_DAY = (By.ID, "days")
    DOB_MONTH = (By.ID, "months")
    DOB_YEAR = (By.ID, "years")
    NEWSLETTER_RADIO_BUTTON = (By.ID, "newsletter")
    OFFERS_RADIO_BUTTON = (By.ID, "optin")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY_NAME = (By.ID, "company")
    ADDRESS1 = (By.ID, "address1")
    ADDRESS2 = (By.ID, "address2")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    CREATE_ACCOUNT = (By.XPATH, "//button[normalize-space()='Create Account']")
    ACCOUNT_CREATED_TEXT = (By.XPATH, "//b[normalize-space()='Account Created!']")
    CONTINUE_BTN = (By.XPATH, "//a[normalize-space()='Continue']")
    LOGGED_IN_AS_FIRSTNAME_TEXT = (By.XPATH, "//li[10]//a[1]")
    DELETE_ACCOUNT = (By.XPATH, "//a[normalize-space()='Delete Account']")
    ACCOUNT_DELETED_TEXT = (By.XPATH, "//b[normalize-space()='Account Deleted!']")

























    # driver.findElement(By.xpath("//input[@id='first_name']"))
    # driver.findElement(By.xpath("//input[@id='last_name']"))
    # driver.findElement(By.xpath("//input[@id='company']"))
    # driver.findElement(By.xpath("//input[@id='address1']"))
    # driver.findElement(By.xpath("//input[@id='address2']"))
    # driver.findElement(By.xpath("//select[@id='country']"))
    # driver.findElement(By.xpath("//input[@id='state']"))
    # driver.findElement(By.xpath("//input[@id='city']"))
    # driver.findElement(By.xpath("//input[@id='zipcode']"))
    # driver.findElement(By.xpath("//input[@id='mobile_number']"))
    # driver.findElement(By.xpath("//button[normalize-space()='Create Account']"))

