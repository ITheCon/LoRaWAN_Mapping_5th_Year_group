#!/usr/bin/env python

import os
import serial
from time import sleep
from datetime import datetime
import time

def getCoord(channel):
        LoRa.write("RD " + str(channel))
        received_data = LoRa.read()
        sleep(0.05)
        data_left = LoRa.inWaiting()
        received_data += LoRa.read(data_left)
        return received_data

def saveData(data, channel):
        now = datetime.now()
        clock = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        USB.write("c" + str(channel) + "," + clock + "," + data)

LoRa = serial.Serial("/dev/ttyS0", 9600, timeout = 10)
USB = serial.Serial("/dev/ttyGS0", 9600)
channels = []

while True:
	LoRa.write("ID " + str(channels))
	resp = LoRa.read()
	sleep(0.05)
	remain = LoRa.inWaiting()
	resp += LoRa.read(remain)
	if (resp == ""):
		break;
	else:
		trim = resp.split()
		channels.append(trim[0])
	sleep(0.5)

if (channels == []):
	quit()

while True:
	start = time.time()
	for channel in channels:
		data = getCoord(channel)
		attempt = 0
		while data == "" and attempt < 2 :
			attempt = attempt + 1
			data = getCoord(channel)
		if data == "" :
			data = "No response,No response\n"
		saveData(data, channel)
	while start+5 > time.time():
		sleep(1)
