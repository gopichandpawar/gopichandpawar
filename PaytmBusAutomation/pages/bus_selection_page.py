from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BusSelectionPage:

    def __init__(self, driver):
        self.driver = driver

    def select_bus(self):

        bus = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[starts-with(@class,'VP3')]//div)[2]"))
        )

        bus.click()

    def select_seat(self):

        seat = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[starts-with(@class,'cK')]//div)[9]"))
        )

        seat.click()

    def click_next(self):

        next_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
        )

        next_btn.click()

    def select_pickup_drop(self):

        pickup = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[starts-with(@class,'iB')]//img)[1]"))
        )

        self.driver.execute_script("arguments[0].click();", pickup)

        drop = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[starts-with(@class,'iB')]//img)[15]"))
        )

        self.driver.execute_script("arguments[0].click();", drop)