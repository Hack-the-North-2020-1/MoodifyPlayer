from services.poll_listeners import register_time_listener
from flask_socketio import join_room, leave_room

# hardcoded images
images = ['https://www.pixelstalk.net/wp-content/uploads/2016/10/HD-Be-Happy-Wallpaper.jpg', 'https://annadannfelt.files.wordpress.com/2015/01/icons-happy-face-10.jpg', 'https://upload.wikimedia.org/wikipedia/en/0/0f/Happy!_Title_Card.png', 'http://i.huffpost.com/gen/1223530/thumbs/o-HAPPY-WOMAN-facebook.jpg', 'http://www.hdwallpaperspulse.com/wp-content/uploads/2012/10/smiley-flower-happy-wallpaper.jpg', 'http://quotesideas.com/wp-content/uploads/2015/06/102377-Happy-Thought-Thursday.jpg', 'https://imgk.timesnownews.com/story/Happy_Daughters_Day.png', 'https://irp-cdn.multiscreensite.com/9f256b4f/dms3rep/multi/Mindfulness-happy.jpg', 'https://www.eharmony.co.uk/dating-advice/wp-content/uploads/2014/03/Happy-flower.jpg', 'https://michiganvirtual.org/wp-content/uploads/2020/01/happy-student-laptop.jpg', 'https://www.fontspring.com/images/kimberly-geswein/kg-happy-1.png', 'https://nhstrategicmarketing.com/wp-content/uploads/2015/04/Happy-Birthday.jpg', 'https://weneedfun.com/wp-content/uploads/2015/05/Happy-Quotes-3.jpg', 'http://kalyaniroldan.com/wp-content/uploads/2012/10/The-Happy-Movie.jpeg', 'https://www.thestatesman.com/wp-content/uploads/2017/11/happy-child.jpg', 'https://www.mccoyrigby.com/wp-content/uploads/sites/6/2016/12/happy-days.jpg', 'https://content.thriveglobal.com/wp-content/uploads/2018/07/happy-dog.jpg', 'http://www.wearemoviegeeks.com/wp-content/uploads/Happy-Happy-Joy-Joy-Key-Art.jpg', 'https://weneedfun.com/wp-content/uploads/2016/09/Happy-Birthday-Wallpapers-26.jpg', 'http://travelsandliving.com/wp-content/uploads/2016/01/adorable-smiling-dogs-24.jpg']

def create_socket(socketio):
    print("creating socket")

    def onSubsribeToImages(data):
        print("client subscribes to images")
        room = data
        join_room(room)
        # note: I use counter_list in here because list is mutable in python
        # another solution is to update the counter by returning it from the pool function
        counter_list = []
        register_time_listener(10, listener, counter_list, room)

    def listener(counter_list, room):
        print("send image")
        socketio.emit("imageData", images[len(counter_list)], room=room)
        counter_list.append(1)

    socketio.on_event("subscribeToImages", onSubsribeToImages)
    return socketio
