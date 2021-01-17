from flask import Blueprint, render_template, session, request, g

from services.spotify import Spotify

blueprint = Blueprint('get_song', __name__)

@blueprint.route('/artist:<artist>&song:<song>')
def get_song(artist, song):
    access_token = request.headers["Authorization"]

    query = f'track:{song} artist:{artist}'
    spotify = Spotify(access_token=access_token)
    id = spotify.search(query)['tracks']['items'][0]['id']

    return { "id": id }