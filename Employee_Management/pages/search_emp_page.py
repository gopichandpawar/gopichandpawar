from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchEmployee:
    def __init__(self,driver):
        self.driver = driver

    def choose_options(self,):
        admin_options = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='oxd-sidepanel-body']//a)[1]"))
        )
        admin_options.click()

    def search_employees(self,emp_name):
        search_emp = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,"(//div//input[@class='oxd-input oxd-input--active'])[2]"))
        )
        search_emp.send_keys(emp_name)

        search = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']"))
        )
        search.click()