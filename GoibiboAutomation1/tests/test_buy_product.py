from pages.home_page import HomePage
from pages.select_bus_page import SelectBusPase

def test_search_bus(driver):
    bus = HomePage(driver)
    bus.enter_from_input("Yavatal")
    bus.enter_to_input("Pune")
    bus.search_result_page()

    bus_selected = SelectBusPase(driver)
    bus_selected.choose_bus_and_select()
    bus_selected.pick_up_and_drop()

