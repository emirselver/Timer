import time
from timer import Timer

timer1 = Timer(timeout=5)
timer2 = Timer(timeout=10)
timer3 = Timer(timeout=15)

all_timers = [timer1, timer2, timer3]

timer1.force_stop(stop_time=3)
timer1.reset()

for timer in all_timers:
    timer.thread.join()
    if timer.timeout:
        print(f"timeout-{timer.timeout_value} ok")
    
print("deneme degisikligi")