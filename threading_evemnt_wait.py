from threading import Thread, Event
from time import sleep
import numpy as np

evnt = Event()

def increase_by_one(array):
    print('Waiting for event')
    l = evnt.wait()
    print('Increasing by one')
    for i in range(len(array)):
        array[i] += 1

data = [1,2,3,4,5,6]
print(data)
t = Thread(target=increase_by_one, args=(data,))
t2 = Thread(target=increase_by_one, args=(data,))
t.start()
t2.start()
for i in range(len(data)):
    data[i] += 1
print('Data Ready. Setting event')
sleep(30)
evnt.set()
t.join()
t2.join()
print(data[0])
print(np.mean(data))
print(data)