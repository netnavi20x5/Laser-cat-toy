import time
import serial
import socket
import random
import math
#ser = serial.Serial(
#  port='COM10',
#  baudrate = 9600,
#)

#EndCom = "\xff\xff\xff"
class ServoCommand:
	StartX=0
	StartY=0
	EndX=0
	EndY=0
	Speed=0
	
	def __init__(self, dist): 
		self.dist = dist
	def servoMove(self,StartX,StartY,EndX,EndY):
		DistX=math.sqrt(math.pow((EndX-StartX))+math.pow((EndY-StartY)))
	def Distance(EndX,EndY):
		self.Dist =math.sqrt(math.pow((EndX-0),2)+math.pow((EndY-0),2))
		return math.sqrt(math.pow((EndX-0),2)+math.pow((EndY-0),2))



ServoMove=ServoCommand


while (True):
#	x = input("Enter X value: ")
#	y = input("Enter Y value: ")
	x = random.randint(50,150)
	y = random.randint(100, 150)
	ServoMove.StartX=x
	ServoMove.Starty=y
	ServoMove.Distance(x,y)
	xy='X'+str(x)+':'+'Y'+str(y)+'\n'
	print (ServoMove.Distance(x,y))
	ServoMove.Dist=ServoMove.Distance(x,y)
	print (ServoMove.Dist)
	print (xy)

#	ser.write(xy.encode())
	time.sleep(0.600)