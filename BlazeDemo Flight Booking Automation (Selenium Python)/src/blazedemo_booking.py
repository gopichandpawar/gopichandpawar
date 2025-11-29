from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time   # ← Missing import (added)

# Setup Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Launch Chrome and open BlazeDemo
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://blazedemo.com/")

# Select departure city
from_city = driver.find_element(By.NAME, "fromPort")
select = Select(from_city)
select.select_by_value("Boston")
time.sleep(2)

# Select destination city
to_city = driver.find_element(By.NAME, "toPort")
select = Select(to_city)
select.select_by_value("London")
time.sleep(2)

# Click "Find Flights"
find_button = driver.find_element(By.XPATH, "//input[@type='submit']")
find_button.click()
time.sleep(2)

# Choose a specific flight (7th option)
flight_option = driver.find_element(By.XPATH, "(//table[@class='table']//input)[7]")
flight_option.click()
time.sleep(2)

try:
    # Enter Name
    name = driver.find_element(By.XPATH, "//input[@id='inputName']")
    name.send_keys("Gopichand")
    time.sleep(2)

    # Enter Address
    address = driver.find_element(By.XPATH, "//input[@id='address']")
    address.send_keys("Hinjawadi")
    time.sleep(2)

    # Enter City
    city = driver.find_element(By.XPATH, "//input[@id='city']")
    city.send_keys("Pune")
    time.sleep(2)

    # Enter State
    state = driver.find_element(By.XPATH, "//input[@id='state']")
    state.send_keys("Maharashtra")
    time.sleep(2)

    # Enter Zip Code
    zipCode = driver.find_element(By.XPATH, "//input[@id='zipCode']")
    zipCode.send_keys("411057")
    time.sleep(2)

    # Select Card Type
    card_type = driver.find_element(By.XPATH, "//select[@id='cardType']")
    select = Select(card_type)
    select.select_by_value("visa")
    time.sleep(2)

    # Enter Credit Card Number
    credit = driver.find_element(By.XPATH, "//input[@id='creditCardNumber']")
    credit.send_keys("123412656765")
    time.sleep(2)

    # Enter Month
    month = driver.find_element(By.XPATH, "//input[@id='creditCardMonth']")
    month.clear()
    month.send_keys("11")
    time.sleep(2)

    # Enter Year
    year = driver.find_element(By.XPATH, "//input[@id='creditCardYear']")
    year.clear()
    year.send_keys("2025")
    time.sleep(2)

    # Enter Name on Card (this was incorrectly mapped earlier)
    card_name = driver.find_element(By.XPATH, "//input[@id='nameOnCard']")
    card_name.send_keys("Debit Card")
    time.sleep(2)

    # Check the "Remember Me" checkbox
    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox.click()
    time.sleep(2)

    # Submit purchase
    submit = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit.click()

except Exception as e:
    print("You are getting an error:", e)