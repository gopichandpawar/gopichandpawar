from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

# Set Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Initialize WebDriver
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Navigate to a page with drag and drop (replace with Rahul Shetty's if needed)
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

# Switch to iframe (specific to jQueryUI site
driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@rel-title='Photo Manager']//iframe[@class='demo-frame']"))

# Find source and target
source = driver.find_element(By.XPATH,"(//div[@class='ui-widget ui-helper-clearfix']//li)[1]" )
target = driver.find_element(By.XPATH, "//div[@id='trash']")

# Perform drag and drop

action = ActionChains(driver)
action.drag_and_drop(source,target).perform()
time.sleep(3)
