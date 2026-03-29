from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#setting chrome options
options = Options()
options.add_experimental_option("detach",True)

#lauching chrome and opening practice
driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

class Login_Page:
    def __init__(self,driver):
        self.driver = driver
        self.username = (By.XPATH,"//input[@name='username']")
        self.password = (By.XPATH,"//input[@name='password']")
        self.submit = (By.XPATH,"//button[@type='submit']")

    def Login(self):
        user = driver.find_element(*self.username)
        user.send_keys("Admin")

        pass1 = driver.find_element(*self.password)
        pass1.send_keys("admin123")

        submit1 = driver.find_element(*self.submit)
        submit1.click()

page1 = Login_Page(driver)
page1.Login()











