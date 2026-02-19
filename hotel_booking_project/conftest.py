import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    #setting chrome options
    options = Options()
    options.add_experimental_option("detach",True)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.booking.com/searchresults.html")

    yield driver
