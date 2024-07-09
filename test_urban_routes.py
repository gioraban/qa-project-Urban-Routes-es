import time #importaciones necesarias para ejecutar las pruebas
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
        routes_page.wait_for_load_field()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)

        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_pedir_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_field()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        button = main.PedirTaxiButton(self.driver)
        button.wait_for_load_button()
        button.click_button_taxi()

    def test_taxi_comfort(self):
        self.driver.get(data.urban_routes_url)
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_field()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        button = main.PedirTaxiButton(self.driver)
        button.wait_for_load_button()
        button.click_button_taxi()
        comfort = main.TaxiComfort(self.driver)
        comfort.wait_for_load_taxi()
        comfort.click_comfort_taxi()
        comfort.click_phone_number_field()

    def test_phone_number_window(self):
        self.driver.get(data.urban_routes_url)
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_field()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        button = main.PedirTaxiButton(self.driver)
        button.wait_for_load_button()
        button.click_button_taxi()
        comfort = main.TaxiComfort(self.driver)
        comfort.wait_for_load_taxi()
        comfort.click_comfort_taxi()
        comfort.click_phone_number_field()
        window = main.PhoneNumberWindow(self.driver)
        window.wait_for_load_head()
        window.set_phone_number(data.phone_number)
        window.click_siguiente_button()
        code = main.retrieve_phone_code(driver=self.driver)
        window.set_sms_code_field(code)
        time.sleep(2)
        window.click_confirmar_button()
        time.sleep(2)

    def test_payment_field(self):
        self.driver.get(data.urban_routes_url)
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_field()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        button = main.PedirTaxiButton(self.driver)
        button.wait_for_load_button()
        button.click_button_taxi()
        comfort = main.TaxiComfort(self.driver)
        comfort.wait_for_load_taxi()
        comfort.click_comfort_taxi()
        comfort.click_phone_number_field()
        window = main.PhoneNumberWindow(self.driver)
        window.wait_for_load_head()
        window.set_phone_number(data.phone_number)
        window.click_siguiente_button()
        code = main.retrieve_phone_code(driver=self.driver)
        window.set_sms_code_field(code)
        window.click_confirmar_button()
        payment_field = main.PaymentField(self.driver)
        payment_field.wait_for_load_pago()
        payment_field.pago_click()

    def test_select_payment(self):
        self.driver.get(data.urban_routes_url)
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_field()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        button = main.PedirTaxiButton(self.driver)
        button.wait_for_load_button()
        button.click_button_taxi()
        comfort = main.TaxiComfort(self.driver)
        comfort.wait_for_load_taxi()
        comfort.click_comfort_taxi()
        comfort.click_phone_number_field()
        window = main.PhoneNumberWindow(self.driver)
        window.wait_for_load_head()
        window.set_phone_number(data.phone_number)
        window.click_siguiente_button()
        code = main.retrieve_phone_code(driver=self.driver)
        window.set_sms_code_field(code)
        window.click_confirmar_button()
        payment_field = main.PaymentField(self.driver)
        payment_field.wait_for_load_pago()
        payment_field.pago_click()
        select_payment = main.SelectPaymentWindow(self.driver)
        select_payment.wait_for_load_cc()
        select_payment.select_cc()

    def test_credit_card_window(self):
        self.driver.get(data.urban_routes_url)
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_field()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        button = main.PedirTaxiButton(self.driver)
        button.wait_for_load_button()
        button.click_button_taxi()
        comfort = main.TaxiComfort(self.driver)
        comfort.wait_for_load_taxi()
        comfort.click_comfort_taxi()
        comfort.click_phone_number_field()
        window = main.PhoneNumberWindow(self.driver)
        window.wait_for_load_head()
        window.set_phone_number(data.phone_number)
        window.click_siguiente_button()
        code = main.retrieve_phone_code(driver=self.driver)
        window.set_sms_code_field(code)
        window.click_confirmar_button()
        payment_field = main.PaymentField(self.driver)
        payment_field.wait_for_load_pago()
        payment_field.pago_click()
        select_payment = main.SelectPaymentWindow(self.driver)
        select_payment.wait_for_load_cc()
        select_payment.select_cc()
        credit_card = main.CreditCardWindow(self.driver)
        credit_card.wait_for_load_card()
        credit_card.set_card_number(data.card_number)
        credit_card.set_card_code(data.card_code)
        credit_card.click_window()
        credit_card.submit_payment()
        credit_card.close_window()
        time.sleep(2)

    def test_message_driver_field(self):
        self.driver.get(data.urban_routes_url)
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_field()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        button = main.PedirTaxiButton(self.driver)
        button.wait_for_load_button()
        button.click_button_taxi()
        comfort = main.TaxiComfort(self.driver)
        comfort.wait_for_load_taxi()
        comfort.click_comfort_taxi()
        comfort.click_phone_number_field()
        window = main.PhoneNumberWindow(self.driver)
        window.wait_for_load_head()
        window.set_phone_number(data.phone_number)
        window.click_siguiente_button()
        code = main.retrieve_phone_code(driver=self.driver)
        window.set_sms_code_field(code)
        window.click_confirmar_button()
        payment_field = main.PaymentField(self.driver)
        payment_field.wait_for_load_pago()
        payment_field.pago_click()
        select_payment = main.SelectPaymentWindow(self.driver)
        select_payment.wait_for_load_cc()
        select_payment.select_cc()
        credit_card = main.CreditCardWindow(self.driver)
        credit_card.wait_for_load_card()
        credit_card.set_card_number(data.card_number)
        credit_card.set_card_code(data.card_code)
        credit_card.click_window()
        credit_card.submit_payment()
        time.sleep(5)
        credit_card.close_window()
        message = main.MessageField(self.driver)
        message.set_message(data.message_for_driver)
        time.sleep(2)

    def test_mantas_panuelos_toggle(self):
        self.driver.get(data.urban_routes_url)
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_field()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        button = main.PedirTaxiButton(self.driver)
        button.wait_for_load_button()
        button.click_button_taxi()
        comfort = main.TaxiComfort(self.driver)
        comfort.wait_for_load_taxi()
        comfort.click_comfort_taxi()
        comfort.click_phone_number_field()
        window = main.PhoneNumberWindow(self.driver)
        window.wait_for_load_head()
        window.set_phone_number(data.phone_number)
        window.click_siguiente_button()
        code = main.retrieve_phone_code(driver=self.driver)
        window.set_sms_code_field(code)
        window.click_confirmar_button()
        payment_field = main.PaymentField(self.driver)
        payment_field.wait_for_load_pago()
        payment_field.pago_click()
        select_payment = main.SelectPaymentWindow(self.driver)
        select_payment.wait_for_load_cc()
        select_payment.select_cc()
        credit_card = main.CreditCardWindow(self.driver)
        credit_card.wait_for_load_card()
        credit_card.set_card_number(data.card_number)
        credit_card.set_card_code(data.card_code)
        credit_card.click_window()
        credit_card.submit_payment()
        time.sleep(5)
        credit_card.close_window()
        time.sleep(2)
        message = main.MessageField(self.driver)
        message.set_message(data.message_for_driver)
        toggle = main.MantasPanuelos(self.driver)
        toggle.click_toggle_select_blanket()
        time.sleep(2)

