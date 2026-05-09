from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest

# ---------- Fixture ----------
@pytest.fixture
def driver():

    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://demo.guru99.com/payment-gateway/index.php")

    yield driver

# ---------- Test Case ----------
def test_payment_gateway(driver):


    # Click Buy Now
    buy_now = WebDriverWait(driver,15).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Buy Now']"))
)
    buy_now.click()

    # Enter Card Number
    card_no = WebDriverWait(driver,15).until(
        EC.element_to_be_clickable((By.ID, "card_nmuber"))
)
    card_no.send_keys("12345678910142563")

    # Select Month
    ex_month = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//select[@id='month']"))
)
    select = Select(ex_month)
    select.select_by_value("3")

    #Select year
    ex_year = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//select[@id='year']"))
)
    select = Select(ex_year)
    select.select_by_value("2020")

    #enter CVV
    cvv_code = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='cvv_code']"))
)
    cvv_code.send_keys("789")

    #click pay
    pay = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='submit']"))
)
    pay.click()

    # Validation
    success_msg = WebDriverWait(driver,15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(),'Payment successfull!')]"))
)

    assert "Payment successfull!" in success_msg.text

    print("Payment Successfully Completed")