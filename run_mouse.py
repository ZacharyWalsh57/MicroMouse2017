'''MicroMouse 2017 - SAC - IEEE
This is the main runtime function for the mouse. All written code is now
being passed into here for final executions.  
'''
import time,random,spidev,numpy,sys,os
import RPi.GPIO as GPIO #LIBS
#The major dependences for this file to compile and run
#All of these libs are called at least once in this file

sys.setrecursionlimit(1000000000)

#Set GPIO pin numbering
GPIO.setmode(GPIO.BCM)

#Initialize right side pins
GPIO.setup(27, GPIO.OUT) #1EN
GPIO.setup(2, GPIO.OUT)  #1A
GPIO.setup(3, GPIO.OUT)  #1B

#Initialize left side pins
GPIO.setup(22, GPIO.OUT) #2EN
GPIO.setup(4, GPIO.OUT)  #2A
GPIO.setup(17, GPIO.OUT) #2B

#Right Back Sensor
GPIO.setup(6, GPIO.IN)
#Left Back Sensor
GPIO.setup(5, GPIO.IN)
#Right Front Sensor
GPIO.setup(15, GPIO.IN)
#Left Front Sensor
GPIO.setup(14, GPIO.IN)
#Front Sensor
GPIO.setup(18, GPIO.IN)

#PWM SETUP
pwm_left=GPIO.PWM(22,200)
pwm_right=GPIO.PWM(27,200)

pwm_left.start(50)
pwm_right.start(50)

#Encoder Setups
GPIO.setmode(GPIO.BCM)
#Right 
GPIO.setup(21, GPIO.IN)
GPIO.setup(20, GPIO.IN)
#left
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

import ANALOG_ARRAY as AnalogArray #FILE
#Used to gather all of our analog values in the maze.
#Also used for a begining sensor zeroing.

import ENCODER_COUNT as encoderCounting #FILR 
#Used for printed output of the nummber of cells the mouse has
#moved.  Also used for eventual stacking/flooding of the maze

import QUEUE_CREATE as queueCreate #FILE
#Used to pass queues around the threads and files of this program
#THE ONLY WAY TO GIVE A QUEUE A NAME AND PRINT IT

import TURN_COUNTER_QUEUE as turnCounter #FILE
#Used to create and modify queues created by the QueueShare class
#The queues are moved arund threads and modified as needed to act
#as counters and lists for the heading.

import DIRECTION_PICKER_QUEUE as directionPicker #FILE
#Used to pick the direction of the mouse.  Relies HEAVILY upon
#the proprer use of the 

import MOVEMENTS_LIB as movements #FILE 
#Library with all of our movements with the correct times
#This IS NOT TO BE TOUCHED SINCE IT IS PERFECT TIMING

import RANDOM_MOVEMENTS as randomMove #FILE 
#Function which is called to initiate the random movements
#of the mouse in the maze. 

import MAZE_MAPPER as mapper #FILE
#Used to change the information about the maze text file is
#presented to us

from threading import Thread
def main():
    AnalogArray.analogArray() #Initalize the AnalogArray
    movementsThread = Thread(target=randomMove.movements) #Start the thread which will move the mouse
    encoderThread = Thread(target=encoderCounting.encoderCounting) #Start the thread that counts cells.
    mapperThread = Thread(target=mapper.mappingWalls) #Maps the walls on the maze
    #mazeSaverThread = Thread(target=mapper.mazeSaver('SAC_MAZE.txt'))

    directionPicker.directionInit(turnCounter.directionQueue)
    
    encoderThread.start() #Start encoders
    movementsThread.start() #Start movements
    mapperThread.start() #Start mapping
    #mazeSaverThread.start() #Start Saving the maze
    time.sleep(5)
    
    encoderThread.join() #Wait for encoders to finish initalizing
    movementsThread.join() #Wait for movements to catch up to CPU/Encoders
    mapperThread.join() #Wait for mapper to get GPIO Setup
    #mazeSaverThread.join()

    
if __name__ == "__main__":
    main()