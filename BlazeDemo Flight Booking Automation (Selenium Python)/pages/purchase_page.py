from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class PurchasePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.ID, "inputName")
    address = (By.ID, "address")
    city = (By.ID, "city")
    state = (By.ID, "state")
    zip_code = (By.ID, "zipCode")
    card_type = (By.ID, "cardType")
    credit_card = (By.ID, "creditCardNumber")
    month = (By.ID, "creditCardMonth")
    year = (By.ID, "creditCardYear")
    name_on_card = (By.ID, "nameOnCard")
    checkbox = (By.XPATH, "//input[@type='checkbox']")
    purchase_btn = (By.XPATH, "//input[@type='submit']")

    def enter_name(self, value):
        self.driver.find_element(*self.name).send_keys(value)

    def enter_address(self, value):
        self.driver.find_element(*self.address).send_keys(value)

    def enter_city(self, value):
        self.driver.find_element(*self.city).send_keys(value)

    def enter_state(self, value):
        self.driver.find_element(*self.state).send_keys(value)

    def enter_zipcode(self, value):
        self.driver.find_element(*self.zip_code).send_keys(value)

    def select_card_type(self, value):
        Select(self.driver.find_element(*self.card_type)).select_by_value(value)

    def enter_credit_card(self, value):
        self.driver.find_element(*self.credit_card).send_keys(value)

    def enter_month(self, value):
        month = self.driver.find_element(*self.month)
        month.clear()
        month.send_keys(value)

    def enter_year(self, value):
        year = self.driver.find_element(*self.year)
        year.clear()
        year.send_keys(value)

    def enter_name_on_card(self, value):
        self.driver.find_element(*self.name_on_card).send_keys(value)

    def click_checkbox(self):
        self.driver.find_element(*self.checkbox).click()

    def click_purchase(self):
        self.driver.find_element(*self.purchase_btn).click()
        time.sleep(2)