import time 
import threading
import concurrent.futures

def register_time_listener(interval, listener, *args):
    def poll():
        while True:
            listener(*args)
            time.sleep(interval)
    # run pool() in a daemon thread
    t = threading.Thread(target=poll, daemon=True)
    t.start()