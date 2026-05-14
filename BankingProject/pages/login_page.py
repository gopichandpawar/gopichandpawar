from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class LoginPage:

    customer_login_btn = (By.CSS_SELECTOR, "button[ng-click='customer()']")
    user_dropdown = (By.ID, "userSelect")
    login_btn = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_customer_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.customer_login_btn)
        ).click()

    def select_customer(self, name):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.user_dropdown)
        )

        Select(dropdown).select_by_visible_text(name)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_btn)
        ).click()