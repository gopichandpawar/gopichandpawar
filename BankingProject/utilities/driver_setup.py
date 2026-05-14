from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():

    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    return driver