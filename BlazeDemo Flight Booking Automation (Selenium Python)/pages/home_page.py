from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    from_port = (By.NAME, "fromPort")
    to_port = (By.NAME, "toPort")
    find_flight_btn = (By.XPATH, "//input[@type='submit']")

    def select_departure_city(self, city):
        Select(self.driver.find_element(*self.from_port)).select_by_value(city)
        time.sleep(2)

    def select_destination_city(self, city):
        Select(self.driver.find_element(*self.to_port)).select_by_value(city)
        time.sleep(2)

    def click_find_flights(self):
        self.driver.find_element(*self.find_flight_btn).click()
        time.sleep(2)