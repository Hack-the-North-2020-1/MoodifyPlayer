import requests, json, base64
from urllib.parse import urlencode

spotify_api_url = "https://api.spotify.com/v1"
oauth_url = "https://accounts.spotify.com/authorize"
api_token_url = "https://accounts.spotify.com/api/token"
redirect_uri = "http://127.0.0.1:5000/auth/callback/spotify"

class Spotify():
    def __init__(self, client_id="", client_secret="", access_token=""):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
    
    def auth_url(self, scope):
        return f"{oauth_url}?client_id={self.client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"

    def get_token(self, code, refresh_token=False):
        client_creds = f"{self.client_id}:{self.client_secret}"

        if refresh_token==True:
            grant_type = 'refresh_token'
            data={
                'client_id': self.client_id,
                'refresh_token': f'{code}',
                'grant_type': grant_type,
                'redirect_uri': redirect_uri
            }
        else:
            grant_type = 'authorization_code'
            data={
                'client_id': self.client_id,
                'code': f'{code}',
                'grant_type': grant_type,
                'redirect_uri': redirect_uri
            }

        client_creds_b64 = base64.b64encode(client_creds.encode())

        headers={ 
            'Accept': 'application/json',
            'Authorization': f'Basic {client_creds_b64.decode()}'
        }

        response = requests.post(api_token_url, data=data, headers=headers).json()

        return response

    def search(self=None, query=None, search_type='track'):

        if isinstance(query, dict):
            query = " ".join([f"{k}:{v}" for k, v in query.items()])

        search_url = urlencode({"q": query, "type": search_type.lower()})
        url = spotify_api_url + '/search?' + search_url
        headers = {'Authorization': f"{self.access_token}"}
        data = requests.get(url, headers=headers).json()

        return data

    @staticmethod
    def find_user(access_token):
        url = spotify_api_url + '/me'
        headers={'Authorization': f"{access_token}"}

        data = requests.get(url, headers=headers).json()
        return data