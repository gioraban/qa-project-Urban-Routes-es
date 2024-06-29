from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_header(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(self.to_field))

    def set_from(self, address_from):
        self.driver.find_element(*self.from_field).send_keys(address_from)

    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, to_address):
        self.wait_for_load_header()
        self.set_from(address_from)
        self.set_to(to_address)
        self.get_to()
        self.get_from()


class PedirTaxiButton:
    button_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_header(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(self.button_taxi))

    def click_button_taxi(self):
        self.driver.find_element(*self.button_taxi).click()

    def click_taxi(self):
        self.wait_for_load_header()
        self.click_button_taxi()


class TaxiComfort:
    comfort_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    phone_number_field = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_header(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(self.comfort_taxi))

    def click_comfort_taxi(self):
        self.driver.find_element(*self.comfort_taxi).click()

    def click_phone_number_field(self):
        self.driver.find_element(*self.phone_number_field).click()

    def taxi_comfort(self):
        self.wait_for_load_header()
        self.click_comfort_taxi()
        self.click_phone_number_field()


class PhoneNumberWindow:
    head = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/div')
    phone_number_field = (By.ID, 'phone')
    siguiente_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    sms_code = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[1]/div')
    confirmar_button = (By.LINK_TEXT, 'Confirmar')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_header(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.head))

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def click_siguiente_button(self):
        self.driver.find_element(*self.siguiente_button).click()

    def retrieve_phone_code(driver) -> str:
        import json
        import time
        from selenium.common import WebDriverException
        code = None
        for i in range(10):
            try:
                logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                        and 'api/v1/number?number' in log.get("message")]
                for log in reversed(logs):
                    message_data = json.loads(log)["message"]
                    body = driver.execute_cdp_cmd('Network.getResponseBody',
                                                 {'requestId': message_data["params"]["requestId"]})
                    code = ''.join([x for x in body['body'] if x.isdigit()])
            except WebDriverException:
                time.sleep(2)
                continue
            if not code:
                raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
            return code

    def set_sms_code_field(self, code):
        self.driver.find_element(*self.sms_code).send_keys(code)

    def get_sms_code(self):
        return self.driver.find_element(*self.sms_code).get_property('value')

    def click_confirmar_button(self):
        self.driver.find_element(*self.confirmar_button).click()

    def  phone_number(self, phone_number, code):
        self.wait_for_load_header()
        self.set_phone_number(phone_number)
        self.get_phone_number()
        self.click_siguiente_button()
        self.retrieve_phone_code()
        self.set_sms_code_field(code)
        self.get_sms_code()
        self.click_confirmar_button()


class UrbanRoutesS:
    metodo_pago_button = (By.CLASS_NAME, 'pp-button filled')
    payment_credit = (By.CLASS_NAME, 'pp-row disabled')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.ID, 'code')
    button_submit_payment = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    button_close_payment = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    message_field = (By.ID, 'comment')
    toggle = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    add_ice_cream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    button_book_taxi = (By.CLASS_NAME, 'smart-button-secondary')
    window_info = (By.CLASS_NAME, 'order-body')
    driver_info = (By.CLASS_NAME, 'order-btn-rating')

    def __init__(self, driver):
        self.driver = driver

    def click_phone_number(self):
        self.driver.find_element(*self.phone_number_field).clic()

    def set_phone_number_field(self, phone_number):
        self.driver.find_element(*self.add_phone_number).send_keys(phone_number)

    def click_siguiente_button(self):
        self.driver.find_element(*self.siguiente_button).click()

    def sms_code_field(self, code):
        self.driver.find_element(*self.sms_code_fiel).send_keys(code)

    def click_confirmar_code(self):
        self.driver.find_element(*self.confirmar_button).click()

    def click_metodo_pago(self):
        self.driver.find_element(*self.metodo_pago_button).click()

    def set_payment_credit(self):
        self.driver.find_element(*self.payment_credit).click()

    def add_card_number_field(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def add_card_code(self, card_code):
        self.driver.find_element(*self.card_code_field).send_keys(card_code).send_keys(Keys.TAB)

    def click_button_submit_payment(self):
        self.driver.find_element(*self.button_submit_payment).click()

    def click_button_close_payment(self):
        self.driver.find_element(*self.button_close_payment).click()

    def click_button_message(self, message_for_driver):
        self.driver.find_element(*self.message_field).send_keys(message_for_driver)

    def click_toggle_select_blanket(self):
        self.driver.find_element(*self.toggle).click()

    def click_add_ice_cream(self):
        self.driver.find_element(*self.add_ice_cream).doubleclick()

    def click_book_taxi(self):
        self.driver.find_element(*self.button_book_taxi).click()

    def wait_until_driver_loaded(self):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(self.driver_info))


