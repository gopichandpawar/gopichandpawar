from selenium.webdriver.common.by import By
import time

class FlightsPage:

    def __init__(self, driver):
        self.driver = driver

    seventh_flight = (By.XPATH, "(//table[@class='table']//input)[7]")

    def choose_flight(self):
        self.driver.find_element(*self.seventh_flight).click()
        time.sleep(2)