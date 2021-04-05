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
        file.write("c" + str(channel) + "," + clock + "," + data)
        file.flush()

LoRa = serial.Serial("/dev/ttyS0", 9600, timeout = 10)
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

now = datetime.now()
clock = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
filename = "/home/pi/data_" + clock + ".csv"
file = open(filename, "a")

while True:
	start = time.time()
	print ("------------------------------------------------")
	for channel in channels:
		print ("Channel: " + channel)
		data = getCoord(channel)
		attempt = 0
		while data == "" and attempt < 2 :
			print ("No response, attempting again")
			attempt = attempt + 1
			data = getCoord(channel)
		if data == "" :
			data = "No response,No response\n"
			print ("No response at all, moving on")
		saveData(data, channel)
		print ("Saved data: " + data)
	while start+5 > time.time():
		sleep(1)
