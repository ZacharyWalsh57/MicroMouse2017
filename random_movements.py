# The Pins to Make the Mouse Move Forward
import RPi.GPIO as GPIO
import time
import random
import TURN_COUNTER_QUEUE as tcq
import DIRECTION_PICKER_QUEUE as dpq
def forward():
		GPIO.output(27, 1)
		GPIO.output(2, 0)
		GPIO.output(3, 1)
		GPIO.output(22, 1)
		GPIO.output(4, 1)
		GPIO.output(17, 0)
		
# The Function to Center the Mouse
def centerMouse():
	if GPIO.input(14) == 0 and GPIO.input(15) == 1 and GPIO.input(5) == 0 and GPIO.input(6) == 0:
		GPIO.output(27, 0)
		GPIO.output(2, 0)
		GPIO.output(3, 0)
		GPIO.output(22, 1)
		GPIO.output(4, 1)
		GPIO.output(17, 0)
		return
	if GPIO.input(15) == 0 and GPIO.input(14) == 1 and GPIO.input(5) == 0 and GPIO.input(6) == 0:
		GPIO.output(27, 1)
		GPIO.output(2, 0)
		GPIO.output(3, 1)
		GPIO.output(22, 0)
		GPIO.output(4, 0)
		GPIO.output(17, 0)
		return		
		
#Move Fwd With Centering.
def moveFwd():
	if GPIO.input(18) == 1 and GPIO.input(6) == 0 and GPIO.input(5) == 0:
		forward()
		centerMouse()
		

#Stop The Mouse mid Run		
def stop():
	GPIO.output(27, 0)
	GPIO.output(2, 0)
	GPIO.output(3, 0)
	GPIO.output(22, 0)
	GPIO.output(4, 0)
	GPIO.output(17, 0)  
	
# The Pins to Make the Mouse Turn Right
def right():
	GPIO.output(27, 1)
	GPIO.output(2, 1)
	GPIO.output(3, 0)
	GPIO.output(22, 1)
	GPIO.output(4, 1)
	GPIO.output(17, 0)
	tcq.turnCounter(1,tcq.rightTurnCounter,tcq.leftTurnCounter,tcq.turnAroundCounter)
	
# The Pins to Make the Mouse Turn Left
def left():
	GPIO.output(27, 1)
	GPIO.output(2, 0)
	GPIO.output(3, 1)
	GPIO.output(22, 1)
	GPIO.output(4, 0)
	GPIO.output(17, 1)
	tcq.turnCounter(2,tcq.leftTurnCounter,tcq.rightTurnCounter,tcq.turnAroundCounter)

#Pins to turn the mouse around
def turnAround():
	GPIO.output(27, 1)
	GPIO.output(2, 0)
	GPIO.output(3, 1)
	GPIO.output(22, 1)
	GPIO.output(4, 0)	
	GPIO.output(17, 1)
	tcq.turnCounter(3,tcq.turnAroundCounter,tcq.rightTurnCounter,tcq.leftTurnCounter)
	time.sleep(.8)

# The Function to Get the Mouse to Turn Right
def turnRight():
	forward()
	time.sleep(.25)
	right()
	time.sleep(.4)
	forward()
	time.sleep(.35)
	return
		
# The Function to Get the Mouse to Turn Left		
def turnLeft():
	forward()
	time.sleep(.25)
	left()
	time.sleep(.45)
	forward()
	time.sleep(.38)
	return
	
# The Function to Get the Mouse to Turn Left Without Moving Forward Before the Turn
def Left():
	left()
	time.sleep(.42)
	forward()
	time.sleep(.38)
	

#The Function to Get the Mouse to Turn Right Without Moving Forward Before the Turn
def Right():
	right()
	time.sleep(.42)
	forward()
	time.sleep(.35)	

# The Function to Get the Mouse to Stop Before Making a Decision	
def reset():
	stop()
	time.sleep(.2)
	
def printDirection():
    dpq.directionPickerLists()	

def movements():
    while True:
		moveFwd()
		# Forced Right Turn
		if GPIO.input(6) == 1 and GPIO.input(5) == 0 and GPIO.input(18)== 0:
			time.sleep(.2)
			if GPIO.input(6) == 1 and GPIO.input(5) == 0 and GPIO.input(18)== 0:
				reset()
				Right()	
				dpq.directionPickerLists()
			
		# Forced Left Turn
		elif GPIO.input(5) == 1 and GPIO.input(6) == 0 and GPIO.input(18) == 0:
			time.sleep(.2)
			if GPIO.input(5) == 1 and GPIO.input(6) == 0 and GPIO.input(18) == 0:
				reset()
				Left()
				dpq.directionPickerLists()
		
		# Y Junction: Straight or Right Turn
		elif GPIO.input(18) == 1 and GPIO.input(5) == 0 and GPIO.input(6) == 1:
			time.sleep(.2)
			if GPIO.input(18) == 1 and GPIO.input(5) == 0 and GPIO.input(6) == 1:
				direction = random.randint(1,2)
				if direction == 1:
					reset()
					moveFwd()
				elif direction == 2:
					reset()
					turnRight()
					dpq.directionPickerLists()

			
		# Y Junction: Straight or Left Turn
		elif GPIO.input(18) == 1 and GPIO.input(6) == 0 and GPIO.input(5) == 1:
			time.sleep(.2)
			if GPIO.input(18) == 1 and GPIO.input(6) == 0 and GPIO.input(5) == 1:
				direction = random.randint(1,2)
				if direction == 1:
					reset()
					moveFwd()
					dpq.directionPickerLists()
				elif direction == 2:
					reset()
					turnLeft()
					dpq.directionPickerLists()
	
		# T Junction: Right Turn or Left Turn
		elif GPIO.input(18) == 0 and GPIO.input(6) == 1 and GPIO.input(5) == 1:
			time.sleep(.2)
			if GPIO.input(18) == 0 and GPIO.input(6) == 1 and GPIO.input(5) == 1:
				direction = random.randint(1,2)
				if direction == 1:
					reset()
					Left()
					dpq.directionPickerLists()
				elif direction == 2:
					reset()
					Right()
					dpq.directionPickerLists()
		
		# Turn the Mouse Around
		elif GPIO.input(18) == 0 and GPIO.input(6) == 0 and GPIO.input(5) == 0:
			time.sleep(.2)
			if GPIO.input(18) == 0 and GPIO.input(6) == 0 and GPIO.input(5) == 0:
				turnAround()
				dpq.directionPickerLists()
		