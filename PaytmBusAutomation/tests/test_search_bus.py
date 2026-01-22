from base.base_driver import BaseDriver
from pages.search_bus_page import SearchBusPage
from utils.config import BASE_URL, FROM_CITY, TO_CITY

class TestSearchBus:

    def test_bus_search(self):
        base = BaseDriver()
        base.launch_url(BASE_URL)

        search_page = SearchBusPage(base.driver, base.wait)

        search_page.enter_from_city(FROM_CITY)
        search_page.enter_to_city(TO_CITY)
        search_page.click_search()
