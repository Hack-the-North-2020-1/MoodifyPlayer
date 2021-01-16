from flask import flash, redirect, render_template, url_for, Blueprint, request, session, g
import json, requests

from models.user import User
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
    access_token = f"Bearer {spotify.get_token(request.args['code'])}"

    if access_token is None:
        flash("Could not authorize request. Try again", 'danger')
        return '', 404

    user = User.signin(access_token)

    session['user_id'] = user.id
    session['access_token'] = access_token

    print('here')
    return redirect(url_for('home.home'))

@blueprint.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.home'))

@blueprint.before_app_request
def get_current_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
        print('No g.user: ', g.user)
    else:
        g.user = User.query.filter_by(id=user_id).first()
        print('Present g.user: ', g.user)