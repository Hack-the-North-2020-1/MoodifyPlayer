from flask import flash, redirect, render_template, url_for, Blueprint, request, session
import json, requests

from settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from services.spotify import Spotify

blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@blueprint.route('/login/spotify')
def spotifyLogin():
    spotify = Spotify(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    return redirect(spotify.auth_url(scope="user-read-email"))

@blueprint.route('/callback/spotify')
def spotifyCallback():
    if 'code' not in request.args:
        return '', 500

    spotify = Spotify(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    access_token = f"Bearer ${spotify.get_token(request.args['code'])}"

    if access_token is None:
        flash("Could not authorize request. Try again", 'danger')
        return '', 404

    session['access_token'] = access_token

    return redirect(url_for('home'))

@blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))