import RPi.GPIO as GPIO

#Set GPIO pin numbering
GPIO.setmode(GPIO.BCM)

#Intialize right side pins
GPIO.setup(27, GPIO.OUT) #1EN
GPIO.setup(2, GPIO.OUT)  #1A
GPIO.setup(3, GPIO.OUT)  #1B

#Initialize left side pins
GPIO.setup(22, GPIO.OUT) #2EN
GPIO.setup(4, GPIO.OUT)  #2A
GPIO.setup(17, GPIO.OUT) #2B

#Stops Mouse
GPIO.output(27, 0)
GPIO.output(2, 0)
GPIO.output(3, 0)
GPIO.output(22, 0)
GPIO.output(4, 0)
GPIO.output(17, 0)