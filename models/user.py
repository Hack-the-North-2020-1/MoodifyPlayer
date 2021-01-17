from services.spotify import Spotify
from extensions import db

class User(db.Model):
    __tablename__ = 'spotify_user'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    profile_url = db.Column(db.String(80), nullable=True)

    def __init__(self, username='', profile_url='', spotify_id=''):
        self.username = username
        self.profile_url = profile_url
        self.spotify_id = spotify_id

    @staticmethod
    def spotify_signin(access_token):
        data = Spotify.find_user(access_token)

        instance = User.query.filter_by(username=data['display_name']).first()

        if not instance:
            if(len(data['images'])):
                instance = User(data['display_name'], data['images'], data['id'])
            
            instance = User(username=data['display_name'], spotify_id=data['id'])
            db.session.add(instance)
            db.session.commit()
        
        return instance