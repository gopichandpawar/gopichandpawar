from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Setting Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Launching Chrome and opening Flipkart
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")

# Enter the value in search box
search = driver.find_element(By.XPATH, "//input[@type='text']")
search.send_keys("Dell Laptop")
search.submit()

# Click on the first product
product = driver.find_element(By.XPATH, "(//div[@data-id]//a)[1]")
print(f"Link: {product.get_attribute('href')}")
print(f"Text: {product.text}")
product.click()

# Switch to the new tab
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])

time.sleep(3)

try:
    #click on the add to the card button
    buy_button = driver.find_element(By.XPATH, "(//div[@class='cPHDOP col-12-12']//button)[1]")
    buy_button.click()
    print("clicked on the 'add to the card' button")

    #click on the plus symbol
    order = driver.find_element(By.XPATH,"//span[contains(text(),'Place Order')]")
    order.click()
    print("clicked on the '+' button")

    #enter the mobile number
    mobile = driver.find_element(By.XPATH,"//input[@type='text']")
    mobile.send_keys("7499552686")

    #click on the continue button
    con_button = driver.find_element(By.XPATH,"//button[@type='submit']")
    con_button.click()
    print("clicked on the continue button")

    #solve manually OTP
    input("Please enter OTP manually in browser, then press Enter here...")

    #click on the login button
    login = driver.find_element(By.XPATH,"//div[@class='col col-5-12']//button[@type='submit']")
    login.click()
    print("clicked on the login button")

except Exception as e:
    print(f"Clicking on error: {e}")
