from pages.login_page import LoginPage

def test_login(driver):

    login = LoginPage(driver)
    login.Login("Admin", "admin123")