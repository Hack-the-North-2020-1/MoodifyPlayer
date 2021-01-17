import requests, json, base64
from urllib.parse import urlencode
from settings import GENIUS_ACCESS_TOKEN
import lyricsgenius

class Genius():

    def get_lyrics(self=None, artist=None, song=None):
        genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)
        artist = genius.search_artist(f'{artist}', max_songs=0, sort="title", include_features=True)
        song = artist.song(f'{song}')
        lyrics = song.lyrics

        return lyrics