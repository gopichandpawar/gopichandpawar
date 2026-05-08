from pages.login_page import LoginPage
from pages.delete_account_page import DeleteAccountPage


def test_delete_account(driver):

    login = LoginPage(driver)
    login.login("mngr660686", "sumeduq")

    delete = DeleteAccountPage(driver)
    delete.delete_account("123456")