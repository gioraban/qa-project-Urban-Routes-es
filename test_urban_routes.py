import time
import data
import main
from selenium import webdriver


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_header()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)

        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_pedir_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_header()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        button = main.PedirTaxiButton(self.driver)
        button.wait_for_load_header()
        button.click_button_taxi()

    def test_taxi_comfort(self):
        self.driver.get(data.urban_routes_url)
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_header()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        button = main.PedirTaxiButton(self.driver)
        button.wait_for_load_header()
        button.click_button_taxi()
        comfort = main.TaxiComfort(self.driver)
        comfort.wait_for_load_header()
        comfort.click_comfort_taxi()
        comfort.click_phone_number_field()

    def test_phone_number_window(self):
        self.driver.get(data.urban_routes_url)
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_header()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        button = main.PedirTaxiButton(self.driver)
        button.wait_for_load_header()
        button.click_button_taxi()
        comfort = main.TaxiComfort(self.driver)
        comfort.wait_for_load_header()
        comfort.click_comfort_taxi()
        comfort.click_phone_number_field()
        window = main.PhoneNumberWindow(self.driver)
        window.wait_for_load_header()
        window.set_phone_number(data.phone_number)
        window.click_siguiente_button()
        window.retrieve_phone_code(driver.se)
        code = retr()
        window.set_sms_code_field(code)
        window.click_confirmar_button()
        time.sleep(2)



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
