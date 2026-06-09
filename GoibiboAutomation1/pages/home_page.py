from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def enter_from_input(self,from_city):
        from_input = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Enter Source']"))
        )
        from_input.send_keys(from_city)

        pick_from_input = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Yavatmal, Maharashtra']"))
        )
        pick_from_input.click()

    def enter_to_input(self, to_city):
        from_input = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Destination']"))
        )
        from_input.send_keys(to_city)

        pick_to_input = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Pune, Maharashtra']"))
        )
        pick_to_input.click()

    def search_result_page(self):
        search_pase = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='searchBusBtn']"))
        )
        search_pase.click()