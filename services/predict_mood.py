import pickle
import spotipy
from spotipy import SpotifyClientCredentials, util

import pandas as pd
import tensorflow as tf

client_id='1d7092e8554d4fd6ae2c882843ede6eb'
client_secret='18bedb36e0ec420f96db8245e7c3664a'

class MusicToMood():

    def __init__(self, client_id = '', client_secret = ''):
        self.manager = SpotifyClientCredentials(client_id,client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=self.manager)
        self.classifier = self._load_classifier()

    def _load_classifier(self):
        with open('ML_models/music_classifier.pkl', 'rb') as fid:
            return pickle.load(fid)
    
    def _get_features_dataframe(self, song_id):
        features = self.sp.audio_features(song_id)

        #construct features dataframe
        d = {"acousticness": [features[0]["acousticness"]], "dancibility": [features[0]["danceability"]], "energy": [features[0]["energy"]], 
            "instrumentalness": [features[0]["instrumentalness"]], "loudness": [features[0]["loudness"]], "speechiness":[features[0]["speechiness"]],
            "valence": [features[0]["valence"]]}
        df = pd.DataFrame(data=d)

        return df

    def predict_mood(self, song_id):
        X_features = self._get_features_dataframe(song_id)
        y_classification =self.classifier.predict(X_features)
        return y_classification[0]

# some testing
musicClassifier = MusicToMood(client_id, client_secret)

# Welcome to New York
print(musicClassifier.predict_mood("6qnM0XXPZOINWA778uNqQ9"))

# Willow
print(musicClassifier.predict_mood("0lx2cLdOt3piJbcaXIV74f"))

# ME!
print(musicClassifier.predict_mood("2Rk4JlNc2TPmZe2af99d45"))

# I'm in here
print(musicClassifier.predict_mood("07OLYWQfwfJKJIwO1heCME"))

# The Man
print(musicClassifier.predict_mood("3RauEVgRgj1IuWdJ9fDs70"))

# Perfect
print(musicClassifier.predict_mood("0tgVpDi06FyKpA1z0VMD4v"))