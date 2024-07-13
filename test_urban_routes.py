import data
import main
import retrieve_phone_code
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
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = main.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_field()
        address_from = data.ADDRESS_FROM
        address_to = data.ADDRESS_TO
        routes_page.set_route(address_from, address_to)

        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_pedir_taxi(self):
        self.test_set_route()
        button = main.PedirTaxiButton(self.driver)
        button.wait_for_load_button()
        button.click_button_taxi()
        button.check_taxi_button()

    def test_taxi_comfort(self):
        self.test_pedir_taxi()
        comfort = main.TaxiComfort(self.driver)
        comfort.wait_for_load_taxi()
        comfort.click_comfort_taxi()
        comfort.check_taxi_comfort()

    def test_phone_number_window(self):
        self.test_taxi_comfort()
        window = main.PhoneNumberWindow(self.driver)
        window.click_ph_number_field()
        window.wait_for_load_head()
        window.set_phone_number(data.PHONE_NUMBER)
        window.click_siguiente_button()
        code = retrieve_phone_code.retrieve_phone_code(driver=self.driver)
        window.set_sms_code_field(code)
        window.click_confirmar_button()
        window.check_ph_number_filled()

    def test_payment_field(self):
        self.test_phone_number_window()
        payment_field = main.PaymentField(self.driver)
        payment_field.wait_for_load_pago()
        payment_field.pago_click()
        payment_field.check_credit_card()

    def test_select_payment(self):
        self.test_payment_field()
        select_payment = main.SelectPaymentWindow(self.driver)
        select_payment.wait_for_load_cc()
        select_payment.select_cc()
        select_payment.check_credit_card_window()

    def test_credit_card_window(self):
        self.test_select_payment()
        credit_card = main.CreditCardWindow(self.driver)
        credit_card.wait_for_load_card()
        credit_card.set_card_number(data.CARD_NUMBER)
        credit_card.set_card_code(data.CARD_CODE)
        credit_card.click_window()
        credit_card.submit_payment()
        credit_card.close_window()
        credit_card.wait_for_load_tarjeta()
        credit_card.check_credit_card_filled()

    def test_message_driver_field(self):
        self.test_credit_card_window()
        message = main.MessageField(self.driver)
        message.set_message(data.MESSAGE_DRIVER)

        assert data.MESSAGE_DRIVER == 'Drive me to Central Park'

    def test_mantas_panuelos_toggle(self):
        self.test_message_driver_field()
        toggle = main.MantasPanuelos(self.driver)
        toggle.click_toggle_select_blanket()

    def test_double_ice_cream(self):
        self.test_mantas_panuelos_toggle()
        ice_cream = main.IceCream(self.driver)
        ice_cream.wait_for_load_ice_cream()
        ice_cream.add_one_ice_cream()
        ice_cream.add_second_ice_cream()
        ice_cream.check_counter_2()

    def test_order_a_taxi(self):
        self.test_double_ice_cream()
        order = main.OrderTaxiModal(self.driver)
        order.click_book_taxi()
        order.wait_for_load_modal()
        order.check_modal()

    def test_info_driver(self):
        self.test_order_a_taxi()
        driver_info = main.InfoDriver(self.driver)
        driver_info.wait_until_driver_loaded()
        driver_info.check_driver_rating()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


