from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_with_otp(self, mobile):

        iframe = self.driver.find_element(By.ID, "oauth-iframe")
        self.driver.switch_to.frame(iframe)

        mobile_number = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "email_mobile_login"))
        )

        mobile_number.send_keys(mobile)

        otp_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@alt='Get OTP']"))
        )

        otp_btn.click()

        otp_field = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "otp_login"))
        )

        otp = input("Enter OTP: ")
        otp_field.send_keys(otp)

        confirm_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Confirm']"))
        )

        confirm_btn.click()

        self.driver.switch_to.default_content()