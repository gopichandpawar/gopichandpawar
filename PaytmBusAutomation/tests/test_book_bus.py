from pages.home_page import HomePage
from pages.bus_selection_page import BusSelectionPage
from pages.login_page import LoginPage
from pages.passenger_page import PassengerPage


def test_paytm_bus_booking(driver):

    home = HomePage(driver)
    bus = BusSelectionPage(driver)
    login = LoginPage(driver)
    passenger = PassengerPage(driver)

    # HOME PAGE
    home.select_from_city("Yavatmal")
    home.select_to_city("Pune")
    home.click_search()

    # BUS PAGE
    bus.select_bus()
    bus.select_seat()
    bus.click_next()

    bus.select_pickup_drop()
    bus.click_next()

    # LOGIN
    login.login_with_otp("7499552687")

    # PASSENGER DETAILS
    passenger.enter_passenger_details(
        "Gopichand Pawar",
        "24",
        "gopichandpawar390@gmail.com"
    )

    passenger.click_proceed()