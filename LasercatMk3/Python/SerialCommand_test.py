import time
import serial
import socket
import random
ser = serial.Serial(
  port='COM10',
  baudrate = 9600,
)

#EndCom = "\xff\xff\xff"
def servoMove(xymove)
	for x in range(xmove[0]):
		print(x)


while (True):
#	x = input("Enter X value: ")
#	y = input("Enter Y value: ")
	x = random.randint(50,150)
	y = random.randint(100, 150)
#	xy='X'+str(x)+':'+'Y'+str(y)+'\n'
#	print (xy)
#	ser.write(xy.encode())
	time.sleep(0.600)