import serial

ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate = 9600,
    timeout=1
)
data = []

def sendData():
    file = open("/home/pi/data_log.csv", "r")
    row = file.readlines() -1
    data = file.readline(row)
    ser.write(str(data).encode('utf-8'))
