from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage

def test_order_buy(driver):

    home = HomePage(driver)
    home.search_product("Hard Disk")
    home.click_on_product()
    home.add_to_card()
    home.proceed_to_buy()

    login =  LoginPage(driver)
    login.enter_mobile("7499552687")
    login.get_otp_on_login_page()

    payment = PaymentPage(driver)
    payment.cash_on_deliver()
    payment.use_pyment_method()
    payment.place_the_order()
