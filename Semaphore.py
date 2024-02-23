import threading


class Semaphore:
    def __init__(self, initial_value) -> None:
        self.lock = threading.Condition(threading.Lock())
        self.value = initial_value
    
    def P(self):
        with self.lock: # context manager - automatically acquire and release the lock
            while self.value <= 0: # if semaphore is zero or less, wait until becomes positive
                self.lock.wait() # block the process from running
                print("waiting")
            self.value -= 1 # decreae the semaphore value

    def V(self):
        with self.lock:
            self.value += 1 # increase the semaphore value
            self.lock.notify() # notify waiting processes or threads that the semaphore value has changed
            print("notified")

    

                
