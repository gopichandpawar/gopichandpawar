import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    option = Options()
    option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get("https://tickets.paytm.com/bus/")

    yield driver
