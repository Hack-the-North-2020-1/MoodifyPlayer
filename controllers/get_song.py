from flask import Blueprint, render_template, session, request, g

blueprint = Blueprint('get_song', __name__)

@blueprint.route('/artist:<artist>&song:<song>')
def get_song(artist, song):

    query = f'track:{song} artist:{artist}'
    spotify = Spotify(access_token=session['spotify_access_token'])
    id = spotify.search(query)['tracks']['items'][0]['id']

    return { "id": id }