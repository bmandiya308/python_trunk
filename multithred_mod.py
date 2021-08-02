import sys
from threading import Lock
import threading as thrd
import time
c = thrd.Condition()

def exceution_block(number):
    print("Entered - ", number)
    c.acquire()
    print("Thread - ",number , "Value - ", number * number)
    time.sleep(600)
    #c.wait() # Release lock
    #c.notify() # call to other thread - one waiting
    #c.notify_all() #c all all waiting thread
    c.release()

number = int(input("Please enter number"))

thread_list = list()
l = Lock()
for num in  range(1,number + 1):
    #print(num)
    thr = thrd.Thread(target=exceution_block,args=(num,))
    thread_list.append(thr)

    thr.start()

for thread in  thread_list:
    thread.join()

sys.exit()


