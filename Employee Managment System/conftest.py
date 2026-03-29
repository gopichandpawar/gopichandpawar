from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_experimental_option("detach",True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield driver
