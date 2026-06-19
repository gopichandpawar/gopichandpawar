from pages.login_page import LoginPage
from pages.search_emp_page import SearchEmployee

def test_search_employee(driver):
    login = LoginPage(driver)
    login.Login("Admin", "admin123")

    emp = SearchEmployee(driver)
    emp.choose_options()
    emp.search_employees("samantha")
