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

def range(checkVal,minVal,maxVal):
	if checkVal >=maxVal:
		return random.randint(minVal,maxVal)
	elif checkVal <=minVal:
		return random.randint(minVal,maxVal)
	else:
		return random.randint(minVal,maxVal)

startX=90
startY=90
#x = random.randint(50,150)
#y = random.randint(100, 150)
x = range(startX,50,150)
y = range(startY,100,150)


while True:
	endX=random.randint(50,150)
	endY=random.randint(100, 150)
	speed = 1;
	
	distance = math.sqrt(math.pow(endX-startX,2)+math.pow(endY-startY,2));
	directionX = (endX-startX) / distance;
	directionY = (endY-startY) / distance;
	
	X = startX;
	Y = startY;
	moving = True
	while moving:
		X += directionX * speed
		Y += directionY * speed
		XY='X'+str(int(X))+':'+'Y'+str(int(Y))+'\n'
		print (XY)
		if(math.sqrt(math.pow(X-startX,2)+math.pow(Y-startY,2)) >= distance):
			X = endX
			Y = endY
			startX=endX
			startY=endY
			XY='X'+str(X)+':'+'Y'+str(Y)+'\n'
			print (XY)
			moving = False
		#time.sleep(0.100)


#while (True):
#	x = input("Enter X value: ")
#	y = input("Enter Y value: ")
#	x = random.randint(50,150)
#	y = random.randint(100, 150)
#	xy='X'+str(x)+':'+'Y'+str(y)+'\n'
#	print (xy)

#	ser.write(xy.encode())
	