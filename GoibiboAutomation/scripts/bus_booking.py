from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------- Chrome Configuration --------------------
options = Options()
options.add_experimental_option("detach", True)

# Launch Chrome browser and open Goibibo Bus page
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.goibibo.com/bus")

try:
    wait = WebDriverWait(driver, 15)

    # -------------------- From City Selection --------------------
    from_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='autosuggestBusSRPSrcHomeName']"))
    )
    from_input.send_keys("Pune")

    from_inp = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@id='downshift-1-item-0']//span)[1]"))
    )
    from_inp.click()

    # -------------------- To City Selection --------------------
    to_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='autosuggest']"))
    )
    to_input.send_keys("Yavatmal")

    to_inp = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@id='downshift-2-item-0']//span)[1]"))
    )
    to_inp.click()

    # -------------------- Search Bus --------------------
    search = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Search Bus']"))
    )
    search.click()

    # -------------------- Select Seat --------------------
    seat = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//div[starts-with(@class,'SrpActiveCardstyles')]//button)[2]"))
    )
    seat.click()

    # -------------------- Select Pickup Point --------------------
    pickup = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//div//input[@type='radio'])[1]"))
    )
    driver.execute_script("arguments[0].click();", pickup)

    # -------------------- Choose Bus Seat --------------------
    seat_sel = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//div[starts-with(@class,'BusBerthstyles__BusO')]//div)[3]"))
    )
    seat_sel.click()

    # -------------------- Continue Booking --------------------
    con_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'CONTINUE')]"))
    )
    con_button.click()

    # -------------------- Passenger Details --------------------
    radio = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='radio']"))
    )
    driver.execute_script("arguments[0].click();", radio)

    name = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Full Name']"))
    )
    name.send_keys("Gopichand Pawar")

    age = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Age']"))
    )
    age.send_keys("25")

    gender = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Female']"))
    )
    gender.click()

    email = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter Email Address']"))
    )
    email.send_keys("gopichandpawar@gmail.com")

    mobile = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter Mobile Number']"))
    )
    mobile.send_keys("7499552689")

    # -------------------- State Selection --------------------
    state = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[text()='State']"))
    )
    state.click()

    maharashtra = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//li[text()='Maharashtra']"))
    )
    maharashtra.click()

    # -------------------- Confirm Details --------------------
    confirm = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='confirm_check' and @type='checkbox']"))
    )
    driver.execute_script("arguments[0].click();", confirm)

    # -------------------- Payment Section --------------------
    pay_but = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[starts-with(@class,'NewReviewstyle__Pay')]"))
    )
    pay_but.click()

    # -------------------- UPI Payment --------------------
    UPI = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@data-testid='paymodeListContent']//li)[1]"))
    )
    UPI.click()

    qr_code = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@data-testid='upiQrBox']//button)[1]"))
    )
    qr_code.click()

    print("✅ Script executed successfully")

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    print("🔚 Test execution completed")