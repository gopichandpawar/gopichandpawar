from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_employees_search_then_edit(driver):
    try:
        username = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        username.send_keys("Admin")

        password = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password.send_keys("admin123")

        login = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        )
        login.click()

        admin = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='oxd-sidepanel-body']//a)[1]"))
        )
        admin.click()

        # click dropdown
        user_role = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]"))
        )
        user_role.click()
        # wait for "Admin" option and click

        admin_option = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-select-option']//span[text()='Admin']"))
        )
        admin_option.click()

        # click dropdown
        user_name = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div//input[@class='oxd-input oxd-input--active'])[2]"))
        )
        user_name.send_keys("Admin")

        # click dropdown
        user_role5 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'oxd-select-wrapper')])[2]"))
        )
        user_role5.click()

        admin_option5 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-select-wrapper']//span[text()='Enabled']"))
        )
        admin_option5.click()

        search = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        search.click()

        edit_emp = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='oxd-table-cell-actions']//button)[2]"))
        )
        edit_emp.click()

        emp_name = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type for hints...']"))
        )
        emp_name.send_keys("ESS")

        change_pass = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))
        )
        driver.execute_script("arguments[0].click();",change_pass)

        save2 = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='oxd-form-actions']//button)[2]"))
        )
        save2.click()

    except Exception as e:
        print("you getting error",e)
