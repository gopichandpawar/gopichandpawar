from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#setting the chrome options
option = Options()
option.add_experimental_option("detach",True)

#lauching chrome and open flipkart application
driver = webdriver.Chrome(options=option)
driver.get("https://www.flipkart.com/")

login = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Login')]"))
)
login.click()

#enter the mobile
mobile = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"(//div[starts-with(@class,'Xi')]//input)"))
)
mobile.send_keys('7499552687')

#click on the request opt
request_otp = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//button[text()='Request OTP']"))
)
request_otp.click()

#enter the OTP
enter_opt = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"(//div[starts-with(@class,'Iv')]//input)"))
)
ent_opt = input("enter the opt:")
enter_opt.send_keys(ent_opt)

login_b = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//button[text()='Verify']"))
)
login_b.click()
