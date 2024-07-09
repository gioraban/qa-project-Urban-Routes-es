from selenium.webdriver.common.by import By #importaciones necesarias para ejecutar las funciones
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#Esta funcion devuelve el codigo sms que recive el Usuario luego de agregar su nuemero de telefono
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


class UrbanRoutesPage: #establece la ruta del  usuario
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_field(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.to_field))

    def set_from(self, address_from):
        self.driver.find_element(*self.from_field).send_keys(address_from)

    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)


class PedirTaxiButton: #ejecuta el boton para pedir el taxi
    button_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.button_taxi))

    def click_button_taxi(self):
        self.driver.find_element(*self.button_taxi).click()


class TaxiComfort: #pide la tarifa Comfort
    comfort_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    phone_number_field = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_taxi(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.comfort_taxi))

    def click_comfort_taxi(self):
        self.driver.find_element(*self.comfort_taxi).click()

    def click_phone_number_field(self):
        self.driver.find_element(*self.phone_number_field).click()


class PhoneNumberWindow: #Agrega el numero telefonico del usuario
    head = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/div')
    phone_number_field = (By.ID, 'phone')
    siguiente_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    sms_code = (By.ID, 'code')
    confirmar_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_head(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.head))

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def click_siguiente_button(self):
        self.driver.find_element(*self.siguiente_button).click()

    def set_sms_code_field(self, code):
        self.driver.find_element(*self.sms_code).send_keys(code)

    def click_confirmar_button(self):
        self.driver.find_element(*self.confirmar_button).click()


class PaymentField: #seleciona la casilla de pago
    pago_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_pago(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.pago_button))

    def pago_click(self):
        self.driver.find_element(*self.pago_button).click()


class SelectPaymentWindow: #selecciona el metodo de pago
    credit_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div/img')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_cc(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.credit_card))

    def select_cc(self):
        self.driver.find_element(*self.credit_card).click()


class CreditCardWindow: #agrega los datos de la tarjeta de credito 
    card = (By.CLASS_NAME, 'card-wrapper')
    card_number_field = (By.ID, 'number')
    code_field = (By.XPATH, '(//*[@id="code"])[2]')
    submit_payment_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_payment_window = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_card(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.card))

    def set_card_number(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def set_card_code(self, card_code):
        self.driver.find_element(*self.code_field).send_keys(card_code)

    def click_window(self):
        self.driver.find_element(*self.card_number_field).click()

    def submit_payment(self):
        self.driver.find_element(*self.submit_payment_button).click()

    def close_window(self):
        self.driver.find_element(*self.close_payment_window).click()


class MessageField: #agrega el mensaje para el  conductor
    message_field = (By.ID, 'comment')

    def __init__(self, driver):
        self.driver = driver

    def set_message(self, message_for_driver):
        self.driver.find_element(*self.message_field).send_keys(message_for_driver)


class MantasPanuelos: #selecciona lel pedido de mantas y panuelos
    toggle = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')

    def __init__(self, driver):
        self.driver = driver

    def click_toggle_select_blanket(self):
        self.driver.find_element(*self.toggle).click()


class IceCream: #ordena dos helados
    add_ice_cream = (By.XPATH,
                     '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')

    def __init__(self, driver):
        self.driver = driver

    def add_one_ice_cream(self):
        self.driver.find_element(*self.add_ice_cream).click()

    def add_second_ice_cream(self):
        self.driver.find_element(*self.add_ice_cream).click()


class OrderTaxi: #se eejeeccuta el pedido del taxi
    button_book_taxi = (By.CLASS_NAME, 'smart-button-secondary')

    def __init__(self, driver):
        self.driver = driver

    def click_book_taxi(self):
        self.driver.find_element(*self.button_book_taxi).click()


class InfoDriver: #espera que aparezca la informacion del driver
    driver_rating = (By.CLASS_NAME, 'order-btn-rating')

    def __init__(self, driver):
        self.driver = driver

    def wait_until_driver_loaded(self):
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(self.driver_rating))
