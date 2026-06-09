from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SelectBusPase:
    def __init__(self,driver):
        self.driver = driver

    def choose_bus_and_select(self):
        choose_b = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"(//div//button[starts-with(@class,'Button-sc')])[4]"))
        )
        choose_b.click()

        select_seat = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[starts-with(@class,'BusBerthstyles__BusOutline')]//div)[27]"))
        )
        select_seat.click()

    def pick_up_and_drop(self):
        pick_up = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@type='radio'])[1]")
            )
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", pick_up)
        self.driver.execute_script("arguments[0].click();", pick_up)

        drop = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@type='radio'])[16]")
            )
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", drop)
        self.driver.execute_script("arguments[0].click();", drop)

        continue1 = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='CONTINUE']")
            )
        )

        continue1.click()