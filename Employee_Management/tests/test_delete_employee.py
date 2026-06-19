from pages.login_page import LoginPage
from pages.delete_page import DeleteEmployee

def test_search_employee(driver):
    login = LoginPage(driver)
    login.Login("Admin", "admin123")

    delete = DeleteEmployee(driver)
    delete.choose_options()
    delete.delete_employees()