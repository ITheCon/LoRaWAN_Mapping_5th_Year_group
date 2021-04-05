import serial
from time import sleep

usb = serial.Serial('/dev/ttyGS0', 9600)

while True :
	file = open('/home/pi/data.csv', 'r')
	for line in file:
		usb.write(line)
		sleep(1)
	file.close()
	usb.write("File end start over\n")
	sleep(2)

