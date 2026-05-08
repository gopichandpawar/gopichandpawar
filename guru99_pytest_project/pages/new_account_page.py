from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def create_account(self, customer_id, deposit):

        # Locate New Account link
        new_account_link = self.wait.until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "New Account")
            )
        )

        # Scroll to element
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            new_account_link
        )

        # JS Click
        self.driver.execute_script(
            "arguments[0].click();",
            new_account_link
        )

        # Customer ID
        self.wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "cusid")
            )
        ).send_keys(customer_id)

        # Initial Deposit
        self.wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "inideposit")
            )
        ).send_keys(deposit)

        # Submit button
        submit_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.NAME, "button2")
            )
        )

        # JS click submit
        self.driver.execute_script(
            "arguments[0].click();",
            submit_btn
        )