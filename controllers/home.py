from flask import Blueprint, render_template, session, request

from services.spotify import Spotify
from services.predict_mood import MusicToMood
from settings import SPOTIFY_CLIENT_SECRET, SPOTIFY_CLIENT_ID

from datetime import datetime, timedelta

import redis


blueprint = Blueprint('home', __name__)

@blueprint.route('/', methods=["POST", "GET"])
def home():

    if 'access_token' in session:
        spotify = Spotify(access_token=session['access_token'])

        if request.method == "POST":
            track = request.form['song_request']
            artist = request.form['artist']
            query = f'track:{track} artist:{artist}'
            print(spotify.search(query)['tracks']['items'][0])
            id = spotify.search(query)['tracks']['items'][0]['id']
            music_to_mood = MusicToMood(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

            data = music_to_mood.predict_mood(id)
            return data

        images = ['https://www.pixelstalk.net/wp-content/uploads/2016/10/HD-Be-Happy-Wallpaper.jpg', 'https://annadannfelt.files.wordpress.com/2015/01/icons-happy-face-10.jpg', 'https://upload.wikimedia.org/wikipedia/en/0/0f/Happy!_Title_Card.png', 'http://i.huffpost.com/gen/1223530/thumbs/o-HAPPY-WOMAN-facebook.jpg', 'http://www.hdwallpaperspulse.com/wp-content/uploads/2012/10/smiley-flower-happy-wallpaper.jpg', 'http://quotesideas.com/wp-content/uploads/2015/06/102377-Happy-Thought-Thursday.jpg', 'https://imgk.timesnownews.com/story/Happy_Daughters_Day.png', 'https://irp-cdn.multiscreensite.com/9f256b4f/dms3rep/multi/Mindfulness-happy.jpg', 'https://www.eharmony.co.uk/dating-advice/wp-content/uploads/2014/03/Happy-flower.jpg', 'https://michiganvirtual.org/wp-content/uploads/2020/01/happy-student-laptop.jpg', 'https://www.fontspring.com/images/kimberly-geswein/kg-happy-1.png', 'https://nhstrategicmarketing.com/wp-content/uploads/2015/04/Happy-Birthday.jpg', 'https://weneedfun.com/wp-content/uploads/2015/05/Happy-Quotes-3.jpg', 'http://kalyaniroldan.com/wp-content/uploads/2012/10/The-Happy-Movie.jpeg', 'https://www.thestatesman.com/wp-content/uploads/2017/11/happy-child.jpg', 'https://www.mccoyrigby.com/wp-content/uploads/sites/6/2016/12/happy-days.jpg', 'https://content.thriveglobal.com/wp-content/uploads/2018/07/happy-dog.jpg', 'http://www.wearemoviegeeks.com/wp-content/uploads/Happy-Happy-Joy-Joy-Key-Art.jpg', 'https://weneedfun.com/wp-content/uploads/2016/09/Happy-Birthday-Wallpapers-26.jpg', 'http://travelsandliving.com/wp-content/uploads/2016/01/adorable-smiling-dogs-24.jpg']

        r = redis.Redis()
        userid = "userid"
        print("store images")
        r.setex(userid, timedelta(minutes=10), value=','.join(images))
            
    return render_template("home/home.html")