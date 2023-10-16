# ESP32-PC
Comunicación entre un esp32 (Con arduino) y una PC usando como interfaz TKinter

Necesario:
ESP32 (Con arduino)
Cable Usb - MicroUsb
Pc con python y pyserial instalado, tkinter y time

El led viene integrado al esp32 que es el pin 2, en caso de querer agregar mas solo modifica el archivo.ino a tu gusto

En la interfaz con tkinter es necesario que uses el boton de Detener todo ya que si lo cierras normalmente con la X de navegacion de windows es posible que crashee y se quede ejecutando un hilo en segundo plano
