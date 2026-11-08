import faker

fake = faker.Faker()

class Config:
    BASE_URL = "https://automationexercise.com/"
    SIGNUP_NAME = "Opeyemi"
    # SIGNUP_EMAIL = "tantether01@tiffincrane.com"
    SIGNUP_EMAIL = fake.email()
    PASSWORD = "P@ssw0rd"
    DOB = [
        {"day": "16", "month": "May", "year": "1978"},
    ]
    LAST_NAME = "Tyson"
    COMPANY = "Fits by Bounce"
    ADDRESS = "13 St Finbarrs' Rd, "
    ADDRESS_2 = "Akoka, Lagos State. Nigeria."
    COUNTRY = "Nigeria"
    STATE = "Lagos"
    CITY = "Akoka"
    ZIPCODE = "100414"
    MOBILE_NUMBER = "2347010898734"

