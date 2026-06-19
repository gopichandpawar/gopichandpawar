from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeleteEmployee:
    def __init__(self,driver):
        self.driver = driver

    def choose_options(self,):
        admin_options = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='oxd-sidepanel-body']//a)[1]"))
        )
        admin_options.click()

    def delete_employees(self):
        delete_emp = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,"(//div[@class='oxd-table-cell-actions']//button)[1]"))
        )
        delete_emp.click()
