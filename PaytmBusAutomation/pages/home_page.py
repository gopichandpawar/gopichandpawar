from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def select_from_city(self, city):

        from_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='dwebSourceInput']"))
        )

        from_input.send_keys(city)

        city_select = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//div[text()='{city}']"))
        )

        city_select.click()

    def select_to_city(self, city):

        to_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='dwebDestinationInput']"))
        )

        to_input.send_keys(city)

        city_select = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//div[text()='{city}']"))
        )

        city_select.click()

    def click_search(self):

        search_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button']"))
        )

        search_btn.click()