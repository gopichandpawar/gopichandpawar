import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    #setting chrome options
    options = Options()
    options.add_experimental_option("detach", True)

    #setting chrome and opening practice page
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()