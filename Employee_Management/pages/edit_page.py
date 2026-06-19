from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditEmployee:
    def __init__(self,driver):
        self.driver = driver

    def choose_options(self,):
        admin_options = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='oxd-sidepanel-body']//a)[1]"))
        )
        admin_options.click()

    def edit_employees(self):
        edit_emp = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,"(//div[@class='oxd-table-cell-actions']//button)[2]"))
        )
        edit_emp.click()

        user_role = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[contains(@class,'oxd-select-wrapper')]//div)[1]"))
        )
        user_role.click()

        choose_options = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-select-wrapper']//span[text()='ESS']"))
        )
        choose_options.click()

        save = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        save.click()