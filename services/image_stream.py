from flask_socketio import join_room, leave_room
import threading
import time

def create_socket(socketio):
    print("creating socket")
    def onSubsribeToImages(data):
        print("client subscribe to image stream")
        room = data
        join_room(room)
        register_time_listener(10, lambda: socketio.emit("imageData", "test data", room=room))
    socketio.on_event("subscribeToImages", onSubsribeToImages)
    return socketio

def register_time_listener(interval, listener):
    def poll():
        while True:
            listener()
            time.sleep(interval)
    # run pool() in a daemon thread
    t = threading.Thread(target=poll, daemon=True)
    t.start()
