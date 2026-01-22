from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SearchBusPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Locators
    FROM_INPUT = (By.ID, "dwebSourceInput")
    FROM_SUGGESTION = (By.XPATH, "//div[contains(text(),'Yavatmal')]")

    TO_INPUT = (By.ID, "dwebDestinationInput")
    TO_SUGGESTION = (By.XPATH, "//div[contains(text(),'Pune')]")

    SEARCH_BUTTON = (By.XPATH, "//button[contains(text(),'Search')]")

    # Actions
    def enter_from_city(self, city):
        self.wait.until(EC.element_to_be_clickable(self.FROM_INPUT)).send_keys(city)
        self.wait.until(EC.element_to_be_clickable(self.FROM_SUGGESTION)).click()

    def enter_to_city(self, city):
        self.wait.until(EC.element_to_be_clickable(self.TO_INPUT)).send_keys(city)
        self.wait.until(EC.element_to_be_clickable(self.TO_SUGGESTION)).click()

    def click_search(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()
