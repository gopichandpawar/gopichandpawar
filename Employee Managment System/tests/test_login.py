from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# setting chrome options
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

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