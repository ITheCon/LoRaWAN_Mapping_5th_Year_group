from datetime import datetime
from time import sleep

while True:
	now = datetime.now()
	print(str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
	sleep(1)
