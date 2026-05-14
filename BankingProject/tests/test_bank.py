from pages.login_page import LoginPage
from pages.customer_page import CustomerPage

def test_banking_flow(driver):

    login = LoginPage(driver)

    login.click_customer_login()
    login.select_customer("Harry Potter")
    login.click_login()

    customer = CustomerPage(driver)

    customer.deposit_amount("5000")

    customer.withdraw_amount("1000")

    customer.open_transactions()

    assert "Transactions" in driver.page_source