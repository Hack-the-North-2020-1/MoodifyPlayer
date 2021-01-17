from flask import Blueprint, render_template, session, request, g

from services.query_image import BingImageQuery
from services.spotify import Spotify
from services.genius import Genius
from services.predict_mood import MusicToMood
from services.keyword_extractor import KeywordExtractor
from settings import SPOTIFY_CLIENT_SECRET, SPOTIFY_CLIENT_ID
from models.user import User
from extensions import db
import os


blueprint = Blueprint('home', __name__)

image_query = BingImageQuery()
extractor = KeywordExtractor()
url_list = []

@blueprint.route('/', methods=["POST", "GET"])
def home():

    if 'spotify_access_token' in session:
        spotify = Spotify(access_token=session['spotify_access_token'])

        if request.method == "POST":
            os.remove("static/urls.txt")
            user_id = session.get('user_id')
            user = User.query.filter_by(id=user_id).first()
            user.image_ready = False
            db.session.commit()
            print(f"start of new post request, url_list: {url_list}")
            track = request.form['song_request']
            artist = request.form['artist']

            lyrics = Genius.get_lyrics(artist=artist, song=track)
            lyrics = lyrics.replace("'", r"\'")

            list_of_keywords = extractor.extract(lyrics)

            query = f'track:{track} artist:{artist}'
            music_to_mood = MusicToMood(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

            id = spotify.search(query)['tracks']['items'][0]['id']
            mood = music_to_mood.predict_mood(id)
            print(f"mood: {mood}, list of keywords: {list_of_keywords}")
            for keyword in list_of_keywords:
                print(f"search term: {mood} {keyword} ")
                image_urls = image_query.query_images(f'{mood} {keyword}', 5)

                with open("static/urls.txt", "a+") as file:
                    for item in image_urls:
                        url_list.append(item)
                        file.write(f"{item} \n")

            user.image_ready = True
            db.session.commit()
            url_list.clear()

    return render_template("home/home.html")