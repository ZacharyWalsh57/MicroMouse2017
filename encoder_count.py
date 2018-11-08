'''Encoder counting.  This is used to count the number of cells moved and 
the number of cells moved in one line before turning around.
This will be used for the dead end filling method.  

CHANGELOG
v1.0 
-Basic code.  This is the first compile that has the variables and commands needed
to allow us to print the cells moved into one single file.  These combined
commands are used to show us the movements.  

v1.1
-Added in a new function that allows us to see how many cells the mouse has moved
forward in a row before changing its direction.  This will allow us to prevent 
going down the same dead ends more than once.  If the code is done correctly in
wallMaker.py then the mouse should be able to pevent many dead ends in the first place.  

'''
import RPi.GPIO as GPIO
import TURN_COUNTER_QUEUE as tcq
import QUEUE_CREATE as Queue
import MAZE_MAPPER as mapper

#Encoder Setups
GPIO.setmode(GPIO.BCM)

#Right 
GPIO.setup(21, GPIO.IN)
GPIO.setup(20, GPIO.IN)
#left
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)


def row_coll_Calc():
    directionList = []
    directionList = list(tcq.directionQueue.queue)
    
    if directionList[0] == 'North':
        rows = list(mapper.rowQueue.queue)
        rows = int(rows[0]) - 2
        print 'ROW ' + str(rows)
        mapper.rowQueue.queue.clear()
        mapper.rowQueue.put(int(rows))
        
    elif directionList[0] == 'South':
        rows = list(mapper.rowQueue.queue)
        rows = int(rows[0]) + 2
        print 'ROW ' + str(rows)
        mapper.rowQueue.queue.clear()
        mapper.rowQueue.put(int(rows))

    elif directionList[0] == 'East':
        colls = list(mapper.collQueue.queue)
        colls = int(colls[0]) + 2
        print 'COLL ' + str(colls)
        mapper.collQueue.queue.clear()
        mapper.collQueue.put(int(colls)) 
            
    elif directionList[0] == 'West':
        colls = list(mapper.collQueue.queue)
        colls = int(colls[0]) - 2 
        print 'COLL ' + str(colls)
        mapper.collQueue.queue.clear()
        mapper.collQueue.put(int(colls)) 


def encoderCounting():
    #This function should be worked into the main movements function for precision.
    #These variables are used to begin counting on the encoders.

    print 'ENCODER COUNTING INIT'
    print 'NO ERRORS HERE MOVE ALONG'
    print 'WAITING 2 SECONDS TO ENSURE CPU IS SYNCHRONIZED'

    global leftPulsesAverage
    global cellsBeforeReverse

    pulse_counter_Right1 = 0
    pulse_counter_Right2 = 0
    pulse_counter_Left1 = 0
    pulse_counter_Left2 = 0
    cellsBeforeReverse = 0
    cellCount = 0
    cellsBeforeReverse = 0
    directionList = list(tcq.directionQueue.queue)

    #Use the local variable of X to constantly continue counting the motor pins
    #Since there are 108 pulses per cell, we can say that the every 108 is one cell.

    while True:

        #Count pulses from Right Encoder
        GPIO.wait_for_edge(21, GPIO.FALLING)
        pulse_counter_Right1 = pulse_counter_Right1+1

        GPIO.wait_for_edge(20, GPIO.FALLING)
        pulse_counter_Right2 = pulse_counter_Right2+1

        #Count pulses from Left Encoder
        GPIO.wait_for_edge(24, GPIO.FALLING)
        pulse_counter_Left1 = pulse_counter_Left1+1

        GPIO.wait_for_edge(23, GPIO.FALLING)
        pulse_counter_Left2 = pulse_counter_Left2+1
        leftPulsesAverage = (pulse_counter_Left1 + pulse_counter_Left2) / 2

        if leftPulsesAverage % 108 == 0:
            cellCount += 1
            print str(cellCount) + ' cells moved'
            row_coll_Calc()
        
              
            