import threading
import time


class Timer:

    def __init__(self, timeout):
        self.timeout_value = timeout
        self.timeout = False
        self.running = True

        self.thread = threading.Thread(target=self.run, name=f"Thread Timeout: {self.timeout_value}",
                                       args=(self.timeout_value, time.time()))
        self.thread.start()

    def force_stop(self, stop_time=None):
        time.sleep(stop_time)
        print(f"{self.thread.name} -> Stopped - Status : {self.timeout}")
        self.running = False

    def reset(self):
        self.running = False
        self.timeout = False
        self.thread.join()
        self.thread = threading.Thread(target=self.run, name=f"Thread Timeout: {self.timeout_value}",
                                       args=(self.timeout_value, time.time()))
        self.running = True
        self.thread.start()

    def run(self, timeout, start_time):

        self.start_time = start_time
        print(f"{self.thread.name} -> Start - Status : {self.timeout}")

        while self.running:
            end_time = time.time()

            if end_time - self.start_time >= timeout:
                self.timeout = True
                print(f"{self.thread.name} -> Finish - Status : {self.timeout}")
                break


