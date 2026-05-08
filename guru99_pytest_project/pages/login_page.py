
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def login(self, userid, password):

        self.driver.get("https://demo.guru99.com/V1/index.php")

        self.wait.until(
            EC.presence_of_element_located((By.NAME, "uid"))
        ).send_keys(userid)

        self.wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        ).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable((By.NAME, "btnLogin"))
        ).click()