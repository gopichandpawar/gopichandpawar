from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MiniStatementPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def mini_statement(self, account_no):

        self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Mini Statement"))
        ).click()

        self.wait.until(
            EC.presence_of_element_located((By.NAME, "accountno"))
        ).send_keys(account_no)

        self.wait.until(
            EC.element_to_be_clickable((By.NAME, "AccSubmit"))
        ).click()