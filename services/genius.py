import requests, json, base64
from urllib.parse import urlencode

genius_api_url = "https://api.genius.com/"
oauth_url = "https://api.genius.com/oauth/authorize"
api_token_url = "https://api.genius.com/oauth/token"
redirect_uri = "http://127.0.0.1:5000/auth/callback/genius"

class Genius():
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

    def search(self=None, query=None):

        if isinstance(query, dict):
            query = " ".join([f"{k}:{v}" for k, v in query.items()])

        search_url = urlencode({"q": query})
        url = genius_api_url + '/search?' + search_url
        headers = {'Authorization': f"{self.access_token}"}
        data = requests.get(url, headers=headers).json()

        return data

    @staticmethod
    def find_user(access_token):
        url = genius_api_url + '/account'
        headers={'Authorization': f"{access_token}"}

        data = requests.get(url, headers=headers).json()
        return data