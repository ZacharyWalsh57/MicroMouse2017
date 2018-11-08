#####################################################################################
#Analog sensor array readings.														#
#This file is used to test the left and right analog sensors and give an average	#
#which will be used in the micromouse for analog turns								#
#Zack Walsh 11-16-16 (Final Build Release)											#
#version 2.1																		#
#####################################################################################
#-----------------------------------------------------------------------------------#
#####################################################################################
#CHANGELOG																			#
#																					#
#v 1.0																				#
#Initial build of the code.  Using one arraay measured five times on the left 		#
#and right sensors.  This proved the be inefficent and in fact the code did not		#
#allow the sensor values to be altered between readings.							#
#																					#
#v 1.1																				#
#Changed basic array creation routine to use numpy in order to conserve time and	#
#CPU usage.  In using numpy, an empty array was created to allow the values to be	#
#appended into the array based on test number and left or right sensor				#
#																					#
#v 2.0																				#
#Complete rewrite of the script. 													#
#Removed original measurement methods												#
#Removed while loops and substutited with counters and if statements				#
#Removed unecessary print statments and substutited with the function seperateLines	#
#which allowed a cleaner code structure												#
#Changed the entire script to remove all nested functions							#
#Made all values that were local -> global for use in both the centering alg		#
#and in the turning algs.															#
#																					#
#v 2.1																				#
#Final build and test run.  This build simply dealt with syntatical errors and		#
#small changes.  Upon running the mouse with this Analog Array, the mouse made it	#
#to the middle of the maze in 59.57 seconds. 										#
#The code is now complete and further versions are not seen necessary unless major	#
#hardware changes are made.  														#
#EOL for development																#
#####################################################################################
'''-------------------------------------------------------------------------------'''

# Analog Setup
import spidev
import time
import os

#Numpy was added and used for more efficent array creation and population
import numpy

spi = spidev.SpiDev()
spi.open(0,0)

def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
  
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts
  
rightSensor= 0 #RIGHT SIDE
leftSensor= 1  #LEFT SIDE

delay = 1 #CHANGE TO MAKE AVERAGE

# Read the right sensor data
rightLevel = ReadChannel(rightSensor)
rightVolts = ConvertVolts(rightLevel,2)
 
# Read the left sensor data
leftLevel = ReadChannel(leftSensor)
leftVolts = ConvertVolts(leftLevel,2)

def seperateLines():
    print ''
    print '------------------------------------------------------------------------------'
    print '------------------------------------------------------------------------------'
    print ''

def analogArray():	
	print 'Here are the average voltages for each side:'
	print ''
	testCounterL = 0
	if testCounterL == 0:
		testV1 = ConvertVolts(leftLevel,2)
		testV2 = ConvertVolts(leftLevel,2)
		testV3 = ConvertVolts(leftLevel,2)
		testV4 = ConvertVolts(leftLevel,2)
		testV5 = ConvertVolts(leftLevel,2)
		testResultsL1 = testV1 , testV2, testV3, testV4, testV5
		testAverageL1 = (testV1 + testV2 + testV3 + testV4 + testV5) / 5
		print 'Test results for the first left side test: ' + str(testResultsL1)
		print 'The average for the first left side test is: ' + str(testAverageL1)
		print ''
		testCounterL = testCounterL + 1
			
	if testCounterL == 1:
		testV1 = ConvertVolts(leftLevel,2)
		testV2 = ConvertVolts(leftLevel,2)
		testV3 = ConvertVolts(leftLevel,2)
		testV4 = ConvertVolts(leftLevel,2)
		testV5 = ConvertVolts(leftLevel,2)
		testResultsL2 = testV1 , testV2, testV3, testV4, testV5
		testAverageL2 = (testV1 + testV2 + testV3 + testV4 + testV5) / 5
		print 'Test results for the second left side test: ' + str(testResultsL2)
		print 'The average for the second left side test is: ' + str(testAverageL2)
		print ''
		testCounterL = testCounterL + 1
			
	if testCounterL == 2:
		testV1 = ConvertVolts(leftLevel,2)
		testV2 = ConvertVolts(leftLevel,2)
		testV3 = ConvertVolts(leftLevel,2)
		testV4 = ConvertVolts(leftLevel,2)
		testV5 = ConvertVolts(leftLevel,2)
		testResultsL3 = testV1 , testV2, testV3, testV4, testV5
		testAverageL3 = (testV1 + testV2 + testV3 + testV4 + testV5) / 5
		print 'Test results for the third left side test: ' + str(testResultsL3)
		print 'The average for the third left side test is: ' + str(testAverageL3)
		testCounterL = testCounterL + 1
			
	seperateLines()
			
	#Collect 3 sets of 5 readings on the mouse at any given time to take averages
			
	testCounterR = 0
	if testCounterR == 0:
		testV1 = ConvertVolts(rightLevel,2)
		testV2 = ConvertVolts(rightLevel,2)
		testV3 = ConvertVolts(rightLevel,2)
		testV4 = ConvertVolts(rightLevel,2)
		testV5 = ConvertVolts(rightLevel,2)
		testResultsR1 = testV1 , testV2, testV3, testV4, testV5
		testAverageR1 = (testV1 + testV2 + testV3 + testV4 + testV5) / 5
		print 'Test results for the first right side test: ' + str(testResultsR1)
		print 'The average for the first right side test is: ' + str(testAverageR1)
		print ''
		testCounterR = testCounterR + 1
			
	if testCounterR == 1:
		testV1 = ConvertVolts(rightLevel,2)
		testV2 = ConvertVolts(rightLevel,2)
		testV3 = ConvertVolts(rightLevel,2)
		testV4 = ConvertVolts(rightLevel,2)
		testV5 = ConvertVolts(rightLevel,2)
		testResultsR2 = testV1 , testV2, testV3, testV4, testV5
		testAverageR2 = (testV1 + testV2 + testV3 + testV4 + testV5) / 5
		print 'Test results for the second right side test: ' + str(testResultsR2)
		print 'The average for the second right side test is: ' + str(testAverageR2)
		print ''
		testCounterR = testCounterR + 1
			
	if testCounterR == 2:
		testV1 = ConvertVolts(rightLevel,2)
		testV2 = ConvertVolts(rightLevel,2)
		testV3 = ConvertVolts(rightLevel,2)
		testV4 = ConvertVolts(rightLevel,2)
		testV5 = ConvertVolts(rightLevel,2)
		testResultsR3 = testV1 , testV2, testV3, testV4, testV5
		testAverageR3 = (testV1 + testV2 + testV3 + testV4 + testV5) / 5
		print 'Test results for the third right side test: ' + str(testResultsR3)
		print 'The average for the third right side test is: ' + str(testAverageR3)
		testCounterR = testCounterR + 1

	seperateLines()
			
	#Make the new populated Array with defined array gen tools
	testDataL = numpy.array([[testResultsL1] , [testResultsL2] , [testResultsL3]])
	leftAverage = (testAverageL1 + testAverageL2 + testAverageL3) / 3
	print 'Left Side Voltages:'
	print testDataL
	print ''
	print 'The Left side sensor voltage average is : ' + str(leftAverage)

	seperateLines()
		
	testDataR = numpy.array([[testResultsR1] , [testResultsR2] , [testResultsR3]])
	rightAverage = (testAverageR1 + testAverageR2 + testAverageR3) / 3
	print 'Right Side Voltages:'	
	print testDataR
	print ''
	print 'The Right side sensor voltage is: ' + str(rightAverage)
			
	seperateLines()
			
	#Calculates and prints the Final Average

	leftAverage = (testAverageL1 + testAverageL2 + testAverageL3) / 3
	print 'Left Side Average: ' + str(leftAverage)
	rightAverage = (testAverageR1 + testAverageR2 + testAverageR3) / 3
	print 'Right Side Average: ' + str(rightAverage)
	print ''	
	finalAverage = (leftAverage + rightAverage) / 2
	print 'Our average voltage is: ' + str(finalAverage)
	print ''