import time 
import threading
import concurrent.futures

import redis

def register_time_listener(interval, listener, *args):
    def poll():
        while True:
            listener(*args)
            time.sleep(interval)
    # run pool() in a daemon thread
    t = threading.Thread(target=poll, daemon=True)
    t.start()

def poll_redis():
    r = redis.Redis()
    while True:
        print("polling redis")
        data = r.get("userid")
        print(data)
        if data is not None:
            images = data.decode("utf-8").split(",")
            print("images are", images)
            # stop the iteration
            return images
        time.sleep(0.5) 