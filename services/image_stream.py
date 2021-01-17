from services.poll_listeners import register_time_listener
from flask_socketio import join_room, leave_room
from flask import session
from models.user import User
from os import path
# hardcoded images

def create_socket(socketio):
    print("creating socket")

    def onSubsribeToImages(data):
        print("client subscribes to images")
        room = data
        join_room(room)
        # note: I use counter_list in here because list is mutable in python
        # another solution is to update the counter by returning it from the pool function
        counter_list = []
        user_id = session.get('user_id')
        user = User.query.filter_by(id=user_id).first()
        register_time_listener(10, listener, counter_list, room, user)

    def listener(counter_list, room, user):
        # print(f"image_ready: {user.image_ready}, user: {user.username}")
        images = []
        print(user)
        if user.image_ready:
            if path.isfile("static/urls.txt"):
                images = open("static/urls.txt").readlines()
            print("send image")
            if images:
                socketio.emit("imageData", images[len(counter_list)], room=room)
            counter_list.append(1)

    socketio.on_event("subscribeToImages", onSubsribeToImages)
    return socketio
