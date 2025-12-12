from selenium.webdriver.common.by import By

SEARCH_BAR = (By.XPATH, "//input[@type='text']")
FIRST_PRODUCT = (By.XPATH, "(//div[@class='a-section a-spacing-base desktop-grid-content-view']//a)[1]")
ADD_TO_CART = (By.XPATH, "//input[contains(@id,'add-to-cart-button')]")
