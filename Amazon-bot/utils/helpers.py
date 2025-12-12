from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_click(driver, locator, timeout=15):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
