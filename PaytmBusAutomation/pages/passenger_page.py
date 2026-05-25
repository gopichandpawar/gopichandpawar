from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PassengerPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_passenger_details(self, name, age_value, email_id):

        passenger_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "fullname"))
        )

        passenger_name.send_keys(name)

        age = self.driver.find_element(By.ID, "age")
        age.send_keys(age_value)

        gender = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Male')]"))
        )

        gender.click()

        email = self.driver.find_element(By.XPATH, "//input[@placeholder='Email ID']")
        email.send_keys(email_id)

    def click_proceed(self):

        proceed = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Proceed To Pay')]"))
        )

        proceed.click()