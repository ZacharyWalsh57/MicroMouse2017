import QUEUE_CREATE as Queue
from threading import Thread
from Queue import PriorityQueue

def turnCounter(turnDirection,queue,queueOff1,queueOff2):
    if turnDirection == 1:
        #print 'Right Turn, adding to queue and turning off the other counters.'
        queue.queue.clear()
        queue.put(1)
        queueOff1.queue.clear()
        queueOff1.put(0)
        queueOff2.queue.clear()
        queueOff2.put(0)


    if turnDirection == 2:
        #print 'Left Turn, adding to queue and turning off the other counters'
        queue.queue.clear()
        queue.put(1)
        queueOff1.queue.clear()
        queueOff1.put(0)
        queueOff2.queue.clear()
        queueOff2.put(0)

    if turnDirection == 3:
        #print 'Turning Around, adding to queue and turning off other counters'
        queue.queue.clear()
        queue.put(1)
        queueOff1.queue.clear()
        queueOff1.put(0)
        queueOff2.queue.clear()
        queueOff2.put(0)


def directionInit(queue):
    direction = 'North'
    queue.put(direction)
    return

leftTurnCounter = Queue.Queue('leftTurn', maxsize=0)
rightTurnCounter = Queue.Queue('rightTurn', maxsize=0)
turnAroundCounter = Queue.Queue('turnAround', maxsize=0)
directionQueue = Queue.Queue('directionQueue')

'''
colls = Queue.Queue('colls')
colls.put(5)

collList = list(colls.queue)
collList = int(collList[0]) - 2
colls.queue.clear()
colls.put(collList)

print colls.queue
'''

'''
testQ = Queue.Queue('testQueue')
testQ.put(10)

testQList = []
testQList = list(testQ.queue)
print testQList[0]

if testQList[0] == 10:
    print 'YES' 

leftCounter = Thread(target=turnCounter, args=(2,leftTurnCounter,rightTurnCounter,turnAroundCounter))
rightCounter = Thread(target=turnCounter, args=(1,rightTurnCounter,leftTurnCounter,turnAroundCounter))
aroundCounter = Thread(target=turnCounter, args=(3,turnAroundCounter,rightTurnCounter,leftTurnCounter))
direction = Thread(target=directionInit, args=(directionQueue,))
'''