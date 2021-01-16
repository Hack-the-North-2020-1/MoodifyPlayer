from flask import Blueprint, render_template, session, request

from services.query_image import BingImageQuery
from services.spotify import Spotify
from services.predict_mood import MusicToMood
from settings import SPOTIFY_CLIENT_SECRET, SPOTIFY_CLIENT_ID


blueprint = Blueprint('home', __name__)

@blueprint.route('/', methods=["POST", "GET"])
def home():

    if 'access_token' in session:
        spotify = Spotify(access_token=session['access_token'])

        if request.method == "POST":
            track = request.form['song_request']
            artist = request.form['artist']
            query = f'track:{track} artist:{artist}'
            id = spotify.search(query)['tracks']['items'][0]['id']
            music_to_mood = MusicToMood(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

            data = music_to_mood.predict_mood(id)

            image_query = BingImageQuery()
            image_query.query_images(f'{data}')

    return render_template("home/home.html")