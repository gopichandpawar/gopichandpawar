from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------------------------------
# Setting Chrome Options
# -------------------------------------------
options = Options()
options.add_experimental_option("detach", True)

# Launch Chrome browser
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.amazon.in/")

# -------------------------------------------
# Close Amazon continue shopping popup (if appears)
# -------------------------------------------
try:
    con_button = driver.find_element(By.XPATH, "//button[text()='Continue shopping']")
    con_button.click()
except Exception:
    pass  # popup may or may not appear

# -------------------------------------------
# Search for the item
# -------------------------------------------
search = driver.find_element(By.XPATH, "//input[@type='text']")
search.send_keys("chair")
search.submit()

# -------------------------------------------
# Click the first product from results
# -------------------------------------------
product = driver.find_element(
    By.XPATH,
    "(//div[@class='a-section a-spacing-base desktop-grid-content-view']//a)[1]"
)
print(f"link: {product.get_attribute('href')}")
print(f"text: {product.text}")
product.click()

# Switch to product window if opened in new tab
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])

# -------------------------------------------
# Add product to cart
# -------------------------------------------
add_cart = driver.find_element(
    By.XPATH,
    "//input[contains(@id,'add-to-cart-button')]"
)
add_cart.click()

# -------------------------------------------
# Handle extended protection popup (if appears)
# -------------------------------------------
try:
    add_pro = driver.find_element(
        By.XPATH,
        "(//div[@class='a-button-stack']//input)[8]"
    )
    driver.execute_script("arguments[0].click();", add_pro)
    print("clicked on add_pro")
except Exception:
    pass

# -------------------------------------------
# Proceed to checkout
# -------------------------------------------
pro_buy = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@value='Proceed to checkout' and @name='proceedToRetailCheckout']")
    )
)
pro_buy.click()

# -------------------------------------------
# Login → Enter Email
# -------------------------------------------
email = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
)
email.send_keys("7499552687")

# Continue button
con_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
)
con_button.click()

# -------------------------------------------
# Enter Password
# -------------------------------------------
password = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
)
password.send_keys("yavatmal@12")

# Click Sign-in
sign_but = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='signInSubmit']"))
)
sign_but.click()

# -------------------------------------------
# Enter OTP
# -------------------------------------------
ent_otp = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@maxlength='6']"))
)

enter_opt = input("Enter the OTP: ")
ent_otp.send_keys(enter_opt)

# Submit OTP
submit = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//div[@class='a-row a-spacing-small']//input)[1]")
    )
)
submit.click()

# -------------------------------------------
# Select Cash on Delivery
# -------------------------------------------
COD = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@class='a-radio']//input)[5]"))
)
driver.execute_script("arguments[0].click();", COD)

# Continue to payment
p_method = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@data-csa-c-slot-id='checkout-primary-continue-payselect']")
    )
)
p_method.click()

# -------------------------------------------
# Place the order
# -------------------------------------------
place_order = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//div[@id='checkout-pyo-button-block']//input)[2]")
    )
)
place_order.click()
