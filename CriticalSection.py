from Semaphore import Semaphore
import time

class CriticalSection:
    def __init__(self) -> None:
        self.semaphore = Semaphore(1)

    def critical_section(self, p):
        # entry section
        self.semaphore.P()

        # CS
        print("Process "+ p + " entered CS")
        time.sleep(5)

        # exit section
        print("Process "+ p + " exiting CS")
        self.semaphore.V()