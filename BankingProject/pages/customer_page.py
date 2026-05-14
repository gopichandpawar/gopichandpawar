from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomerPage:

    deposit_btn = (By.CSS_SELECTOR, "button[ng-click='deposit()']")
    withdraw_btn = (By.CSS_SELECTOR, "button[ng-click='withdrawl()']")
    transaction_btn = (By.CSS_SELECTOR, "button[ng-click='transactions()']")

    amount_input = (By.CSS_SELECTOR, "input[ng-model='amount']")
    submit_btn = (By.CSS_SELECTOR, "button[type='submit']")

    message = (By.CSS_SELECTOR, "span.error")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def deposit_amount(self, amount):

        self.wait.until(
            EC.element_to_be_clickable(self.deposit_btn)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.amount_input)
        ).send_keys(amount)

        self.wait.until(
            EC.element_to_be_clickable(self.submit_btn)
        ).click()

    def withdraw_amount(self, amount):

        self.wait.until(
            EC.element_to_be_clickable(self.withdraw_btn)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.amount_input)
        ).send_keys(amount)

        self.wait.until(
            EC.element_to_be_clickable(self.submit_btn)
        ).click()

    def open_transactions(self):

        self.wait.until(
            EC.element_to_be_clickable(self.transaction_btn)
        ).click()