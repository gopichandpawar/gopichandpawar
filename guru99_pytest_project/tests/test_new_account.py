from pages.login_page import LoginPage
from pages.new_account_page import NewAccountPage


def test_new_account(driver):

    login = LoginPage(driver)
    login.login("mngr660686", "sumeduq")

    account = NewAccountPage(driver)
    account.create_account("12345", "5000")