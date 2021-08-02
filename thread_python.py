import threading as thread
from threading import Lock
import time
def f(l, i):
    l.acquire()
    #time.sleep(10)
    try:
        #num = 10//i
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        thread.Thread(target=f, args=(lock, num)).start()
        #thread.Thread(target=f, args=(lock, num)).start()