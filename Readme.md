# Proyecto Urban Routes
  



*En este proyecto se trata de automatizar el servicio para solicitar un taxi en la pagina web de Urban Rutes con el patron POM. Para ello se necesita que el usuario realize una serie de pasos tales como, seleccionar la ruta, escoja el modo del automovil deseado, agregue su numero de telefono y  la tarjeta de credito.*  


**Iniciamos clonando el repositorio `qa-project-Urban-Routes-es`en la computadora. En la terminal crea un directorio para almacenar el proyecto. Por ejemplo:**

    `cd ~`
    `mkdir projects`   
    `cd projects`

**Asegurate de clonar el repositorio correcto:**

` git clone git@github.com:username/qa-project-Urban-Routes-es.git`

**Trabajar con la copia de manera local. Es importante leer bien las instrucciones del ejecicio 1 del proyecto 8 de la pagina de Tripleten antes de compenzar el proyecto.**

**En esta seencuentra el enlace de Urban Routes para realizar las pruebas necesarias de la automatizacion requerida.**

**Es necesario importar selenium para poder realizar la automatizacion. Dentro de cada archivo importaremos otros soportes requeridos adicionalmente a selenium, dependiendo de las necesidades de cada prueba.**

## El proyecto Urban Routes cuenta con tres archivos:

1. Data.py, este archivo cuenta con los datos necesarios para realizar la automatizacion.

    1. El URL de la pagina web.
    2. Las variantes de las direcciones Desde y Hacia.
    3. La variante del numero de telefono del usuario,
    4. Las variantes de los datos de la tarjeta de credito.
    5. La variante del mensaje para el coductor.

2. Main.py, en este archivo se encuentra:

    i. Las importaciones:
    
       `from selenium.webdriver.common.by import By` Esta importacion es necesaria parala busqueda de los elementos.
    
       `from selenium.webdriver.support import expected_conditions` Esta importacion es necesaria para saber que es lo que se esta esperando en el metodo `Explicit Wait`
    
       `from selenium.webdriver.support.wait import WebDriverWait` Esta importacion es necesaria para la pagina web espere y se ejecute el metodo `Explicit Wait`.
    
    ii. La funcion `def` interpreta el codigo de autenticacion del numero de telefono del usuario. Finaliza con el metodo `return` del codigo, ya que  es requerida la confimacion del numero de telefono. La variante del codigo se utilizara en la prueba del relleno del campo telefono.
     
        `def retrieve_phone_code(driver) -> str:`

    iii. El metodo  `Explicit Wait` se encuentra en aquellas clases donde se cambian de pantalla y por lo tanto es necesario un poco mas de tiempo para encontrar el elemento solicitado. 
    
    iv. Todas las clases tienen como primer metodo __int__ para establecer el Driver.

    v. Cada clase contiene los localizadores necesarios para ubicar dichos elementos en la pagina y poder realizar las interacciones con funciones.  
    
**Listado de las Clases:**

`class UrbanRoutesPage:` En esta clase se utilizan los metodo `get` y `return` para establecer la ruta del usuario.
    
`class PedirTaxiButton:` Esta clase es para hacer click en el boton Pedir un Taxi.
    
`class TaxiComfort:` Esta clase es para seleccionar la tarifa Comfort, haciendo click en el elemento asignado.
    
`class PhoneNumberWindow:`Se crea una clase para la ventana de Agregar Numero Telefono y luego aparezca en la casilla de numero de telefono.
    
`class PaymentField:` Esta clase en la hacer click en el campo de Metodo de Pago y abrir la ventana de pago.
    
`class SelectPaymentWindow:` Esta clase es para hacer click en Credict Card, y seleccionarlo como  Metodo de Pago. Se abrira otra ventana.
    
`class CreditCardWindow:` En esta clase se almacena la informacion de la tarjeta de credito del usuario. Para eso es necesario perder el enfoque con otro click y poder habilitar el boton Agregar. Luego se debe cerrar la ventana anterior haciendo click en el boton X. 
    
`class MessageField:` Esta clase es para escribir el mensaje al condutor.
    
`class MantasPanuelos:` Esta clase es para hacer click en el toggle y poder seleccionar las Mantas y los Panuelos.

`class IceCream:` En esta clase se usa el metodo click dos en dos funciones distintas para seleccionar dos helados.
    
`class OrderTaxi:`  En esta clase se hace click  en el boton para finalizar la orden y pedir un taxi.
    
`class InfoDriver:` En esta clase se utiliza el metodo `Explicit Wait` para ubicar el raiting del conductor y asi lograr el comedito de visualizar la ventana que contiene la informacion del viaje.. 

3. Test_urban_routes.py, en este archivo se ejecutan la pruebas de automatizazon para pedir un taxi con el patron POM.
 
     1. Comenzamos con el metodo de clase `@classmethod`  y el metodo `setup_class(cls)` declarando a clase como un argumento y controlando el driver,en mi caso Chrome.
     2. En la clase Test Urban Routes hay 12 pruebas para comprobar la automatizacion de Urban Routes Page.
        1. `def test_set_route(self):`  Verifica la configuracion de las direcciones en los campos Desde y Hasta. Se utilizan las direcciones que se encuentra en el archivo Data.
        2. `def test_pedir_taxi(self):` Prueba boton Pedir un Taxi.
        3. `def test_taxi_comfort(self):` Prueba la seleccion de la tarifa Comfort y abre la ventana para introducir el numero telefonico.
        4. `def test_phone_number_window(self):` Agrega el numero de telefono que se enccuentra en Data, y recibe el codigo sms que se enccuentra en la funcion `def retrieve_phone_code(driver) -> str:` que se encuentra en el  archivo Main
        5. `def test_payment_field(self):` Abre la ventana de Metodo de pago.
        6. `def test_select_payment(self):` Prueba la seleccion dde pago Agregar tarjeta, abre una nueva ventana.
        7. `def test_credit_card_window(self):` Prueba que se agreguen los datos en los campos Numero de tarjeta y en Codigo. Dicgos datos se encuentran en el archivo Data. Hay que cambiar el enfoque para que el boton Agregar se active, almacenar los datos y volver a la pantalla principal.
        8. `def test_message_driver_field(self):` Comprueba que se pueda escribir un mensaje al conductor, el mensaje se encuentra en el archivo Data.
        9. `def test_mantas_panuelos_toggle(self):` Comprueba que se puede hacer click en el toggle y pedir la manta y el panuelo.
        10. `def test_double_ice_cream(self):` Comprueba que se pueda ordenar dos helados haciendo click en el boton `+` dos veces.
        11. `def test_order_a_taxi(self):` Comprobar el boton de reserva y que aparesca la ventana que Buscar taxi.
        12. `def test_info_driver(self):` Crea un tiempo de espera para comprobar que aparezca la ventana con la informacion del conductor.
     
     iii. El metodo `teardown_class()` finaliza las pruebas  cerrando el navegador y detiene el driver.
   
   ### Conclusión del Proyecto Urban Routes

En el proyecto Urban Routes, se automatizó el servicio de solicitud de taxis en la página web utilizando el patrón Page Object Model (POM). Esto incluye pasos como seleccionar rutas, elegir el tipo de automóvil, ingresar un número de teléfono y proporcionar detalles de pago.

El proyecto se compone de tres archivos: **Data.py**, que contiene los datos necesarios para las pruebas; **Main.py**, que define las clases y la lógica de automatización; y **Test_urban_routes.py**, donde se ejecutan las pruebas.

Cada clase maneja un aspecto específico del proceso de solicitud, permitiendo una organización clara y eficiente. Las pruebas abarcan desde la configuración de direcciones hasta la finalización del pedido, garantizando que todas las funcionalidades sean correctas.

Finalmente, el uso de métodos como `setup_class` y `teardown_class` asegura una gestión adecuada del entorno de prueba, facilitando un inicio y cierre efectivos del navegador. Este proyecto destaca la eficacia de la automatización en la mejora de la experiencia del usuario en Urban Routes.

## Muchas gracias!!!
### Georgina Khamisso
