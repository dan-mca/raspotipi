import base64
import requests
from urllib.parse import urlencode, quote_plus
from dotenv import load_dotenv
import os

class SpotifyAuth:
    def __init__(self):
        load_dotenv('.env')
        self.spotify_auth_url = 'https://accounts.spotify.com/authorize?'
        self.spotify_token_url = 'https://accounts.spotify.com/api/token'
        self.client_id = os.environ.get('client_id')
        self.client_secret = os.environ.get('client_secret')
        self.response_type = 'code'
        self.redirect_uri = 'http://127.0.0.1:5000/redirect'
        self.scope = os.environ.get('scope').replace(' ', '%20')
        self.encoded = base64.b64encode(bytes(self.client_id + ':' + self.client_secret, 'utf-8'))

    def get_auth_url(self):
        payload = {'client_id':self.client_id, 'client_secret': self.client_secret,
                    'response_type': 'code', 'redirect_uri': self.redirect_uri,
                    'scope': self.scope}
        url_params = urlencode(payload, quote_via=quote_plus)
        return self.spotify_auth_url + url_params
    
    def get_access_token(self, code):
        code = code
        payload = {'grant_type': 'authorization_code', 'code': code, 'redirect_uri': 'http://127.0.0.1:5000/redirect'}
        headers = {'Authorization': f'Basic {self.encoded.decode()}'}
     
        response = requests.post(self.spotify_token_url, data=payload, headers=headers)
        token_info = response.json()

        return token_info

    def refresh_token(self):
        token_info = self.get_access_token()
        refresh_token = token_info["refresh_token"]

        response = requests.post(self.spotify_token_url,
                                data={"grant_type": "refresh_token", "refresh_token": refresh_token},
                                headers={"Authorization": f"Basic {self.encoded.decode()}"})

        response_json = response.json()

        return response_json["access_token"] 