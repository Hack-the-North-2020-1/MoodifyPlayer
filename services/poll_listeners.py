import time 
import threading

def register_time_listener(interval, listener):
    def poll():
        while True:
            listener()
            time.sleep(interval)
    # run pool() in a daemon thread
    t = threading.Thread(target=poll, daemon=True)
    t.start()