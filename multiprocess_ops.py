from multiprocessing import Process, Lock
import time
def f(l, i):
    print('BEFORE LOCK', i)
    l.acquire()
    try:
        print('hello world', i)
        time.sleep(5)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()