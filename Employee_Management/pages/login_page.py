from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def Login(self,username1,password1):
        username = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,"//input[@name='username']"))
        )
        username.send_keys(username1)

        password = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password.send_keys(password1)

        login = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        login.click()