from pages.login_page import LoginPage
from pages.edit_page import EditEmployee

def test_search_employee(driver):
    login = LoginPage(driver)
    login.Login("Admin", "admin123")

    edit = EditEmployee(driver)
    edit.choose_options()
    edit.edit_employees()