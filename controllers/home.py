from flask import Blueprint, render_template, session, request, g

from services.query_image import BingImageQuery
from services.spotify import Spotify
from services.genius import Genius
from services.predict_mood import MusicToMood
from services.keyword_extractor import KeywordExtractor
from settings import SPOTIFY_CLIENT_SECRET, SPOTIFY_CLIENT_ID


blueprint = Blueprint('home', __name__)

image_query = BingImageQuery()
extractor = KeywordExtractor()

@blueprint.route('/', methods=["POST", "GET"])
def home():

    if 'spotify_access_token' in session:
        spotify = Spotify(access_token=session['spotify_access_token'])

        if request.method == "POST":
            track = request.form['song_request']
            artist = request.form['artist']

            lyrics = Genius.get_lyrics(artist=artist, song=track)
            lyrics = lyrics.replace("'", r"\'")

            list_of_keywords = extractor.extract(lyrics)

            query = f'track:{track} artist:{artist}'
            music_to_mood = MusicToMood(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

            id = spotify.search(query)['tracks']['items'][0]['id']
            mood = music_to_mood.predict_mood(id)
            for keyword in list_of_keywords:
                image_urls = image_query.query_images(f'{mood} {keyword}', 5)
                #append url
            #set image ready to true

    return render_template("home/home.html")