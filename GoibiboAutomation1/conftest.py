import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def driver():
    options = Options()
    options.add_experimental_option("detach",True)

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.goibibo.com/bus/")
    driver.maximize_window()
    yield driver
