import TURN_COUNTER_QUEUE as tcq
import time

def directionInit(queue):   
    queue.put('North')

def directionPickerLists():
    directionList = []
    directionList = list(tcq.directionQueue.queue)

    counterRight = []
    counterRight = list(tcq.rightTurnCounter.queue)
    #print counterRight[0]

    counterLeft = []
    counterLeft = list(tcq.leftTurnCounter.queue)
    #print counterLeft[0]

    counterReverse = []
    counterReverse = list(tcq.turnAroundCounter.queue)
    #print counterReverse[0]

    if directionList[0] == 'North':
        try:
            if counterRight[0] == 1:
                tcq.directionQueue.queue.clear()
                tcq.directionQueue.put('East')
                directionList = ['East']
                print ''
                print 'HEADED: ' + directionList[0] + '\n'
                directionList = []
            elif counterLeft[0] == 1:
                tcq.directionQueue.queue.clear()
                tcq.directionQueue.put('West')
                directionList = ['West']
                print ''
                print 'HEADED: ' + directionList[0] + '\n'
                directionList = []
            elif counterReverse[0] == 1:
                tcq.directionQueue.queue.clear()
                tcq.directionQueue.put('South')
                directionList = ['South']
                print ''
                print 'HEADED: ' + directionList[0] + '\n'
                directionList = []
        except:
            print 'INDEX_ERROR' + '\n'
            pass

    elif directionList[0] == 'South':
        try:
            if counterRight[0] == 1:
                tcq.directionQueue.queue.clear()
                tcq.directionQueue.put('West')
                directionList = ['West']
                print ''
                print 'HEADED: ' + directionList[0] + '\n'
                directionList = []
            elif counterLeft[0] == 1:
                tcq.directionQueue.queue.clear()
                tcq.directionQueue.put('East')
                directionList = ['East']
                print ''
                print 'HEADED: ' + directionList[0] + '\n'
                directionsList = []
            elif counterReverse[0] == 1:
                tcq.directionQueue.queue.clear()
                tcq.directionQueue.put('North')
                directionList = ['North']
                print ''
                print 'HEADED: ' + directionList[0] + '\n'
                directionList = []
        except:
            print 'INDEX_ERROR'
            pass

    elif directionList[0] == 'East':
        try:
            if counterRight[0] == 1:
                tcq.directionQueue.queue.clear()
                tcq.directionQueue.put('South')
                directionList = ['South']
                print ''
                print 'HEADED: ' + directionList[0] + '\n'
                directionList = []
            elif counterLeft[0] == 1:
                tcq.directionQueue.queue.clear()
                tcq.directionQueue.put('North')
                directionList = ['North']
                print ''
                print 'HEADED: ' + directionList[0] + '\n'
                directionsList = []
            elif counterReverse[0] == 1:
                tcq.directionQueue.queue.clear()
                tcq.directionQueue.put('West')
                directionList = ['West']
                print ''
                print 'HEADED: ' + directionList[0] + '\n'
                directionList = []
        except:
            print 'INDEX_ERROR'
            pass

    elif directionList[0] == 'West':
        try:
            if counterRight[0] == 1:
                tcq.directionQueue.queue.clear()
                tcq.directionQueue.put('North')
                directionList = ['North']
                print ''
                print 'HEADED: ' + directionList[0] + '\n'
                directionList = []
            elif counterLeft[0] == 1:
                tcq.directionQueue.queue.clear()
                tcq.directionQueue.put('South')
                directionList = ['South']
                print ''
                print 'HEADED: ' + directionList[0] + '\n'
                directionsList = []
            elif counterReverse[0] == 1:
                tcq.directionQueue.queue.clear()
                tcq.directionQueue.put('East')
                directionList = ['East']
                print ''
                print 'HEADED: ' + directionList[0] + '\n'
                directionList = []
        except:
            print 'INDEX_ERROR'
            pass

'''
Runtime Examples

directionInit(tcq.directionQueue) #Start direction of North

print 'Current DIR: ' + str(tcq.directionQueue.queue)
tcq.turnCounter(3,tcq.turnAroundCounter,tcq.rightTurnCounter,tcq.leftTurnCounter) #Sets turn around
directionPickerLists() #Checks directio
print''

print 'Current DIR: ' + str(tcq.directionQueue.queue)
tcq.turnCounter(3,tcq.turnAroundCounter,tcq.rightTurnCounter,tcq.leftTurnCounter) #Sets turn around
directionPickerLists() #Checks direction
print ''

'''





