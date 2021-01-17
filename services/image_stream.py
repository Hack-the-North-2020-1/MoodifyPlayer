from services.poll_listeners import register_time_listener, poll_redis
from flask_socketio import join_room, leave_room

def create_socket(socketio):
    print("creating socket")

    def onSubsribeToImages(data):
        print("client subscribes to images")
        room = data
        join_room(room)
        # note: I use counter_list in here because list is mutable in python
        # another solution is to update the counter by returning it from the pool function
        # pull redis if 
        images = poll_redis()
        counter_list = []
        register_time_listener(10, listener, counter_list, images, room)

    def listener(counter_list, images, room):
        print("send image")
        print(images)
        socketio.emit("imageData", images[len(counter_list)], room=room)
        counter_list.append(1)

    socketio.on_event("subscribeToImages", onSubsribeToImages)
    return socketio
        
