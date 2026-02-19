from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.ID, "login")

    def load(self):
        self.driver.get("https://adactinhotelapp.com/")

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_button).click()

