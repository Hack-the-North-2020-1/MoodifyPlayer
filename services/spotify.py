import requests, json, base64

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

    def get_token(self, code):
        client_creds = f"{self.client_id}:{self.client_secret}"

        client_creds_b64 = base64.b64encode(client_creds.encode())

        headers={ 
            'Accept': 'application/json',
            'Authorization': f'Basic {client_creds_b64.decode()}'
        }
        
        data={
            'client_id': self.client_id,
            'code': code, 
            'grant_type': "authorization_code",
            'redirect_uri': redirect_uri
        }

        response = requests.post(api_token_url, data=data, headers=headers).json()

        return response.get('access_token', None)

    @staticmethod
    def find_user(access_token):
        url = spotify_api_url + '/me'
        headers={'Authorization': f"{access_token}"}

        data = requests.get(url, headers=headers).json()
        return data