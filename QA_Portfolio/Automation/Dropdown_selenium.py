from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

#setting chrome options
options = Options()
options.add_experimental_option("detach",True)

#launhcing chrome and open practice page
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#choose the select options
val = driver.find_element(By.ID,"dropdown-class-example")

select = Select(val)
select.select_by_index(2)
time.sleep(2)
select.select_by_value("option2")
time.sleep(2)
select.select_by_visible_text("Option3")