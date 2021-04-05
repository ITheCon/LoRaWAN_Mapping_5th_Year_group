import serial

usb = serial.Serial('/dev/ttyGS0', 9600)

data = "Hello"

usb.write(data)

usb.close()
