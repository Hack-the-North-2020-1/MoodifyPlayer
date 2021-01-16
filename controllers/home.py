from flask import Blueprint, render_template, session, request

from services.spotify import Spotify
from services.predict_mood import MusicToMood

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
            music_to_mood = MusicToMood('1d7092e8554d4fd6ae2c882843ede6eb', '18bedb36e0ec420f96db8245e7c3664a')
            data = music_to_mood.predict_mood(id)
            return data

    return render_template("home/home.html")