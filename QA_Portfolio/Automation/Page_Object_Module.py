from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Setting Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Launching Chrome and opening login page
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5.5)
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

# Page Object Model for Login Page
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "input-email")
        self.password = (By.ID, "input-password")
        self.Login_btn = (By.XPATH, "//input[@type='submit']")

    def login(self):
        self.driver.find_element(*self.username).send_keys("gopichandpawar390@gmail.com")
        self.driver.find_element(*self.password).send_keys("yavatmal12")
        self.driver.find_element(*self.Login_btn).click()

# Using the page
page = LoginPage(driver)
page.login()