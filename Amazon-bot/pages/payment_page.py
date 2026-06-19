from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentPage:
    def __init__(self,driver):
        self.driver = driver

    def cash_on_deliver(self):
        cash_on_d = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"(//div//input[@type='radio'])[6]"))
        )
        self.driver.execute_script("arguments[0].click();", cash_on_d)

    def use_pyment_method(self):
        use_payment = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"(//div//input[@type='submit'])[3]"))
        )
        use_payment.click()

    def place_the_order(self):
        place_order = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"(//div//input[@id='placeOrder'])[4]"))
        )
        place_order.click()