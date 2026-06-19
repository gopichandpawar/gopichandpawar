from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def enter_mobile(self,mobile1):
        mobile = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='ap_email_login']"))
        )
        mobile.send_keys(mobile1)

        continue1 = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@type='submit']"))
        )
        continue1.click()

    def get_otp_on_login_page(self):
        choose_opt = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='continue']"))
        )
        choose_opt.click()

        get_opt = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@name='code']"))
        )
        otp = input("enter OTP:")
        get_opt.send_keys(otp)

        verify = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@aria-label='Verify OTP Button']"))
        )
        verify.click()