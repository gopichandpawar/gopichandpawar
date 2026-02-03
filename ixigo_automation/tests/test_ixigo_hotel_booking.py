import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_ixigo_hotel_booking(driver):

    wait = WebDriverWait(driver, 30)

    # ================== ENTER CITY ==================
    input_city = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter city, area or property name']")
        )
    )
    input_city.click()
    input_city.clear()
    input_city.send_keys("Pune")

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//p[normalize-space()='Pune']")
        )
    ).click()

    # ================== CLICK SEARCH ==================
    search = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@data-testid='search-hotels']")
        )
    )
    driver.execute_script("arguments[0].click();", search)

    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@data-testid='bpg-home-modal']//button")
            )
        ).click()
        print("clicked on the popup")
    except:
        print("not clicked on the popup")

    time.sleep(3)

    # ================== CLICK BOOK NOW ==================
    bus_book = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//button[normalize-space()='Book Now'])[1]")
        )
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", bus_book)
    driver.execute_script("arguments[0].click();", bus_book)

    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])

    # ================== Reserve one Room ==================
    reserve1 = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//div[starts-with(@class,'flex gap')]//button)[1]")
        )
    )
    driver.execute_script("arguments[0].click();", reserve1)

    # ================== enter the mobile number ==================
    mobile = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter Mobile Number']")
        )
    )
    mobile.send_keys("7499552687")

    continue1 = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[text()='Continue']")
        )
    )
    continue1.click()

    ent_otp = input("enter the OTP:")

    inter_otp = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@inputmode='numeric']")
        )
    )
    inter_otp.clear()
    inter_otp.send_keys(ent_otp)

    verify = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[text()='Verify']")
        )
    )
    driver.execute_script("arguments[0].click();", verify)

    # ================== SECOND RESERVE ==================
    reserve2 = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//div[starts-with(@class,'flex gap')]//button)[1]")
        )
    )
    driver.execute_script("arguments[0].click();", reserve2)

    # ================== Person Details ==================
    name = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='firstName-input']")
        )
    )
    name.send_keys("Gopichand")

    last_name = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='lastName-input']")
        )
    )
    last_name.send_keys("Pawar")

    email = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='email-input']")
        )
    )
    email.send_keys("gopichandpawar@gmail.com")

    pay_now = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@data-testid='payment-btn']")
        )
    )
    pay_now.click()

    debit_cart = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[text()='Credit/Debit/ATM Card']")
        )
    )
    debit_cart.click()

    card_num = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@data-testid='card-number']")
        )
    )
    card_num.send_keys("1234567890123456")

    exp_date = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@data-testid='card-exp-date']")
        )
    )
    exp_date.send_keys("326")

    cvv = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@data-testid='new-card-cvv']")
        )
    )
    cvv.send_keys("245")

    sec_pay = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@id='btn-paymentForm-newCard']")
        )
    )
    sec_pay.click()
print("✅ Flow completed till payment page")

