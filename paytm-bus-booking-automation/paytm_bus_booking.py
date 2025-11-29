from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setting Chrome options
option = Options()
option.add_experimental_option("detach", True)

#Launching chrome and opening ticket paytm
driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://tickets.paytm.com/bus/")

# ------------------------- STEP 1: FROM CITY -----------------------------
try:
    from_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='dwebSourceInput']"))
    )
    from_input.send_keys("Yavatmal")

    f_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='Yavatmal']"))
    )
    f_input.click()
except Exception as e:
    print("Error selecting FROM city:", e)

# ------------------------- STEP 2: TO CITY -----------------------------
try:
    to_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='dwebDestinationInput']"))
    )
    to_input.send_keys("Pune")

    t_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='Pune']"))
    )
    t_input.click()
except Exception as e:
    print("Error selecting TO city:", e)

# ------------------------- STEP 3: SEARCH BUS ---------------------------
try:
    search_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='button']"))
    )
    search_btn.click()
    print("Bus search started!")
except Exception as e:
    print("Error clicking Search button:", e)

# ------------------------- STEP 4: SEAT SELECTION -----------------------
try:
    Bus_s = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[starts-with(@class,'VP3')]//div)[4]"))
    )
    Bus_s.click()

    seat_c = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[starts-with(@class,'cK')]//div)[24]"))
    )
    seat_c.click()
    print("Seat selected!")
except Exception as e:
    print("Error selecting seat:", e)

# ------------------------- STEP 5: NEXT BUTTON --------------------------
try:
    next_c = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
    )
    next_c.click()
except Exception as e:
    print("Error clicking Next:", e)

# --------------------- PICKUP & DROP RADIO BUTTONS ---------------------
try:
    pickup_you = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//div[starts-with(@class,'iB')]//img)[1]"))
    )
    driver.execute_script("arguments[0].click();", pickup_you)

    drop_you = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//div[starts-with(@class,'iB')]//img)[15]"))
    )
    driver.execute_script("arguments[0].click();", drop_you)
except Exception as e:
    print("Error selecting pickup/drop:", e)

# ------------------------- NEXT BUTTON AGAIN ---------------------------
try:
    next_a = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
    )
    next_a.click()
except Exception as e:
    print("Error clicking Next:", e)

# ------------------------- LOGIN IFRAME -------------------------------
try:
    iframe = driver.find_element(By.ID, "oauth-iframe")
    driver.switch_to.frame(iframe)

    mobile_number = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "email_mobile_login"))
    )
    mobile_number.send_keys("7499552687")

    OTP_B = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@alt='Get OTP']"))
    )
    OTP_B.click()

    OTP_E = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "otp_login"))
    )

    OTP_enter = input("Enter OTP: ")
    OTP_E.send_keys(OTP_enter)

    con_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Confirm']"))
    )
    con_button.click()

except Exception as e:
    print("Error during OTP login:", e)

# ------------------------ PASSENGER DETAILS ----------------------------
try:
    passenger_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fullname"))
    )
    passenger_name.send_keys("Gopichand Pawar")

    age = driver.find_element(By.ID, "age")
    age.send_keys("24")

    gender = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Male')]"))
    )
    gender.click()

    email = driver.find_element(By.XPATH, "//input[@placeholder='Email ID']")
    email.send_keys("gopichandpawar390@gmail.com")

    proceed = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Proceed To Pay')]"))
    )
    proceed.click()

except Exception as e:
    print("Error entering passenger details:", e)

# -------------------------- PAYMENT SECTION ----------------------------
try:
    credit_card = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Credit and Debit Cards')]"))
    )
    credit_card.click()

    card_number = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='cardNumber' and @name='cardNumber']"))
    )
    card_number.send_keys("1212121212121212")

    # switching the iframe
    iframe = driver.find_element(By.XPATH, "//iframe[starts-with(@class,'ptm-card-iframe')]")
    driver.switch_to.frame(iframe)

    # FIX XPATH BELOW — YOU MUST ENTER CORRECT XPATH
    date_and_month = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='MM/YY']"))
    )
    date_and_month.send_keys("12/25")

    CVV = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='CVV']"))
    )
    CVV.send_keys("123")

    pay_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//div[starts-with(@class,'ptm-body-bg ptm-pos-a ptm-btn-wra')]//button)[1]"))
    )
    pay_button.click()
    print("You have filled card details!")

except Exception as e:
    print("Error in payment section:", e)
