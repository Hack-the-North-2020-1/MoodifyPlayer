from services.poll_listeners import register_time_listener
from flask_socketio import join_room, leave_room

def create_socket(socketio):
    print("create socket")
    def onSubsribeToImages(data):
        print("client subsribe to images")
        room = data
        join_room(room)
        register_time_listener(10, lambda: socketio.emit("imageData", "test data", room=room))
    socketio.on_event("subscribeToImages", onSubsribeToImages)
    return socketio
