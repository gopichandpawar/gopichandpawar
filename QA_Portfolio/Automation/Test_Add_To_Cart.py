from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#settting options
options = Options()
options.add_experimental_option("detach",True)

#lauching chrome options
driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.in/")

try:
    val = driver.find_element(By.XPATH,"//button[@type='submit']")
    val.click()
    print("clicked")

except:
    print("not click")

#value in search bar
search = driver.find_element(By.XPATH,"//input[@type='text']")
search.send_keys("laptop bag")
search.submit()

#click on the product
product = WebDriverWait(driver,5).until(
    EC.element_to_be_clickable((By.XPATH,"(//div[@class='aok-relative']//a)[1]")))

print(f"link: {product.get_attribute('href')}")
print(f"text: {product.text}")
product.click()

#swith to the window
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])

try:
    # Click on 'Add to Cart' button
    add_pro = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[starts-with(@id,'add-to-cart-button')]"))
    )
    add_pro.click()
    print("Added to cart")

    # Click on 'Go to Cart' button
    go_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/cart?ref_=sw_gtc')]"))
    )
    go_cart.click()
    print("Opened cart")

    # Optional: wait for the gift checkbox (may not always be present)
    try:
        checkbox = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='sc-buy-box-gift-checkbox']"))
        )
        checkbox.click()
        print("Gift checkbox clicked")
    except:
        print("Gift checkbox not found (skipped)")


except Exception as e:
    print(f"Error: {e}")