import pyfirmata
port = pyfirmata.Arduino("COM6")
x=port.get_pin('d:13:0')