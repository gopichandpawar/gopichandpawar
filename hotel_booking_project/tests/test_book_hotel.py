from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def test_book_hotel(driver):
    # ------------------ Search Hotel ------------------

    # Enter city name
    search_hotel = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Where are you going?']"))
    )
    search_hotel.send_keys("Pune")

    # Select suggestion from dropdown
    suggest_pune = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//div//div[text()='Pune'])[1]"))
    )
    suggest_pune.click()

    # Click search button
    search_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    search_button.click()

    # ------------------ Close Sign-in Popup (if appears) ------------------

    try:
        popup = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Dismiss sign-in info.']"))
        )
        popup.click()
        print("Clicked on dismiss popup")
    except Exception as e:
        print("No popup appeared:", e)

    # ------------------ Select First Hotel ------------------

    click_first_hotel = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//div//a[@data-testid='availability-cta-btn'])[1]"))
    )
    click_first_hotel.click()

    # Switch to new tab if opened
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])

    # ------------------ Select Room ------------------

    select_room = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "(//div//select[@class='hprt-nos-select js-hprt-nos-select'])[1]"))
    )
    select = Select(select_room)
    select.select_by_value("1")

    # Click reserve button
    reserve = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//div[starts-with(@class,'hprt-reservation')]//button)[1]"))
    )
    reserve.click()

    # ------------------ Person Details ------------------

    name = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='firstname' and @type='text']"))
    )
    name.send_keys("Gopichand")

    last_name = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='lastname' and @type='text']"))
    )
    last_name.send_keys("Pawar")

    email = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='email' and @type='email']"))
    )
    email.send_keys("gopichandpawar39@gmail.com")

    mobile = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='phoneNumber']"))
    )
    mobile.send_keys("7499552689")

    # Accept checkbox
    check_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//div//input[@type='checkbox'])[1]"))
    )
    check_box.click()

    # Submit final details
    final_detail = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
    )
    final_detail.click()

    # Confirm booking
    com_booking = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    com_booking.click()

    print("Booking Completed")
