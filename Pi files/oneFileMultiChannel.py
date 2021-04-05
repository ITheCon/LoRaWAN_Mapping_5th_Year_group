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
transaction = 0
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
print (channels)
if (channels == []):
	quit()

now = datetime.now()
clock = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
filename = "/home/pi/ftp/GPSsheets/data_" + clock + ".csv"
file = open(filename, "a")

while True:
	start = time.time()
	transaction += 1
	print ("------------ Transaction " + str(transaction) + " ------------")
	for channel in channels:
		data = getCoord(channel)
		attempt = 0
		while data == "" and attempt < 2 :
			attempt = attempt + 1
			print ("Attempt " + str(attempt) + " failed, trying again")
			data = getCoord(channel)
		if data == "" :
			data = "No response,No response\n"
		print ("T" + str(transaction) + ": Channel " + str(channel) + ": " + data)
		saveData(data, channel)
	        print ("T" + str(transaction) + ": Written")
	print ("---------------------------------------")
	while start+60 > time.time():
		sleep(1)
