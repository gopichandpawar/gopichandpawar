from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# setting chrome options
options = Options()
options.add_experimental_option("detach", True)

#launching chrome and opening flipkart application
driver = webdriver.Chrome(options=options)
driver.get("https://www.flipkart.com/")

# enter the value in search bar
search = driver.find_element(By.XPATH, "//input[@name='q']")
search.send_keys("Laptop")
search.submit()