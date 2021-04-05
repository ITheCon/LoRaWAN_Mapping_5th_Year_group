# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:52:34 2021

@author: Ozzyb
"""

import serial

s = serial.Serial("COM11", 9600)

while True:
    res = s.read()
    left = s.inWaiting()
    res += s.read(left)
    print(res)