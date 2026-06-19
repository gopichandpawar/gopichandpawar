from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def search_product(self,product_name):
        search = WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,"//input[@id='twotabsearchtextbox']"))
        )
        search.send_keys(product_name)
        search.submit()

    def click_on_product(self):
        product = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"(//div[@class='aok-relative']//a)[1]"))
        )
        print(f"text: {product.text}")
        print(f"link: {product.get_attribute('href')}")
        product.click()

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

    def add_to_card(self):
        add_product = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//input[contains(@id,'add-to-cart-button')]"))
        )
        add_product.click()

    def proceed_to_buy(self):
        proceed = WebDriverWait(self.driver,15).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@name='proceedToRetailCheckout']"))
        )
        proceed.click()



