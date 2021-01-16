from flask import Blueprint, render_template, session, request

from services.query_image import BingImageQuery
from services.spotify import Spotify
from services.genius import Genius
from services.predict_mood import MusicToMood
from settings import SPOTIFY_CLIENT_SECRET, SPOTIFY_CLIENT_ID


blueprint = Blueprint('home', __name__)

@blueprint.route('/', methods=["POST", "GET"])
def home():

    if 'spotify_access_token' and 'genius_access_token' in session:
        spotify = Spotify(access_token=session['spotify_access_token'])
        genius = Genius(access_token=session['genius_access_token'])

        if request.method == "POST":
            track = request.form['song_request']
            artist = request.form['artist']

            spotify_query = f'track:{track} artist:{artist}'
            genius_query = f'{track} {artist}'
            music_to_mood = MusicToMood(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

            id = spotify.search(query)['tracks']['items'][0]['id']
            spotify_data = music_to_mood.predict_mood(id)
            genius_data = genius.search(genius_query)

            data = {'spotify': spotify_data, 'genius': genius_data}
            image_query = BingImageQuery()
            image_query.query_images(f'{data}')

    return render_template("home/home.html")