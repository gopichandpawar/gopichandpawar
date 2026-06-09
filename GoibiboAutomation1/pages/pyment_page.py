from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentBusPase:
    def __init__(self,driver):
        self.driver = driver

    def click_check_box(self):
        check_box = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@name='cancel']"))
        )
        self.driver.execute_script("arguments[0].click();", check_box)

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

    def  passenger_details(self):
        fullname = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Enter Full Name']"))
        )
        fullname.send_keys("Gopichand Pawar")

        age1 = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Age']"))
        )
        age1.send_keys("24")

        male1 = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Male']"))
        )
        male1.click()

        email1 = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Email Address']"))
        )
        email1.send_keys("gopichandpawar390@gmail.com")

        mobile = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Mobile Number']"))
        )
        mobile.send_keys("7499552687")

    

