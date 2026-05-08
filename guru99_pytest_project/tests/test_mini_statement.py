from pages.login_page import LoginPage
from pages.mini_statement_page import MiniStatementPage


def test_mini_statement(driver):

    login = LoginPage(driver)
    login.login("mngr660686", "sumeduq")

    mini = MiniStatementPage(driver)
    mini.mini_statement("123456")