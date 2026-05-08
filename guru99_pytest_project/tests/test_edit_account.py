from pages.login_page import LoginPage
from pages.edit_account_page import EditAccountPage

def test_edit_account(driver):

    login = LoginPage(driver)
    login.login("mngr660686", "sumeduq")

    edit = EditAccountPage(driver)
    edit.edit_account("123456")