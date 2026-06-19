import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def driver():
    #setting chrome options
    options = Options()
    options.add_experimental_option("detach",True)

    #setting chrome options
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.amazon.in/")

    yield driver

