import pytest
from pages.home_page import HomePage
from pages.flights_page import FlightsPage
from pages.purchase_page import PurchasePage

@pytest.mark.usefixtures("setup")
class TestBookFlight:

    def test_flight_booking(self):

        home = HomePage(self.driver)

        home.select_departure_city("Boston")
        home.select_destination_city("London")
        home.click_find_flights()

        flights = FlightsPage(self.driver)
        flights.choose_flight()

        purchase = PurchasePage(self.driver)

        purchase.enter_name("Gopichand")
        purchase.enter_address("Hinjawadi")
        purchase.enter_city("Pune")
        purchase.enter_state("Maharashtra")
        purchase.enter_zipcode("411057")

        purchase.select_card_type("visa")

        purchase.enter_credit_card("123412656765")
        purchase.enter_month("11")
        purchase.enter_year("2025")
        purchase.enter_name_on_card("Debit Card")

        purchase.click_checkbox()
        purchase.click_purchase()