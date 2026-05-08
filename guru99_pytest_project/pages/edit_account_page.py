from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EditAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def edit_account(self, account_no):

        # Locate Edit Account link
        edit_link = self.wait.until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "Edit Account")
            )
        )

        # Scroll into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            edit_link
        )

        # JS click to avoid intercepted click issue
        self.driver.execute_script(
            "arguments[0].click();",
            edit_link
        )

        # Enter account number
        self.wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "accountno")
            )
        ).send_keys(account_no)

        # Click submit
        submit_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.NAME, "AccSubmit")
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            submit_btn
        )