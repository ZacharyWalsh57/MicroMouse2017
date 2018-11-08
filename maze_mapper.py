import numpy #Maze creation and moficiation
import TURN_COUNTER_QUEUE as tcq #Seeing if the direction is changing/confirming with turns
import DIRECTION_PICKER_QUEUE as dpq #Seeing if the direction has changed
import MODIFY_THIS_MAZE as maze #Creates the maze for this file to modify
import QUEUE_CREATE as Queue
import RPi.GPIO as GPIO
import time

collQueue = Queue.Queue('coll')
collQueue.put(1)
rowQueue = Queue.Queue('rows')
rowQueue.put(31)




def mazeSaver(fileName):
        numpy.savetxt(fileName, maze.maze, delimiter = ' ', newline='\r\n', fmt="%-2s")
        time.sleep(2)

def mappingWalls():
    rowList = list(rowQueue.queue)
    row = int(rowList[0])

    collList = list(collQueue.queue)
    coll = int(collList[0])

    direction = []
    direction = list(tcq.directionQueue.queue)

    while True:
        sacMaze = open('sacMaze.txt', 'w+')
        

        rowList = list(rowQueue.queue)
        row = int(rowList[0])

        collList = list(collQueue.queue)
        coll = int(collList[0])

        direction = []
        direction = list(tcq.directionQueue.queue)

        if direction[0] == 'North':   
            if GPIO.input(5) == 0:
                maze.maze[row,(coll-1)] = '|'
            if GPIO.input(6) == 0:
                maze.maze[row,(coll+1)] = '|'
            if GPIO.input(18) == 0:
                maze.maze[(row-1), coll] = '--'

        if direction[0] == 'South':
            if GPIO.input(5) == 0:
                maze.maze[row,(coll+1)] = '|'
            if GPIO.input(6) == 0:
                maze.maze[row,(coll-1)] = '|'
            if GPIO.input(18) == 0:
                maze.maze[(row+1), coll] = '--'

        if direction[0] == 'East':
            if GPIO.input(5) == 0:
                maze.maze[(row+1),coll] = '--'
            if GPIO.input(6) == 0:
                maze.maze[(row-1),coll] = '--'
            if GPIO.input(18) == 0:
                maze.maze[row,(coll-1)] = '|'

        if direction[0] == 'West':
            if GPIO.input(5) == 0:
                maze.maze[(row-1),coll] = '--'
            if GPIO.input(6) == 0:
                maze.maze[(row+1),coll] = '--'
            if GPIO.input(18) == 0:
                maze.maze[row,(coll+1)] = '|'
        
        else:
            numpy.savetxt(sacMaze, maze.maze)
            
            


