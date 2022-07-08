from urllib.parse import urljoin
import requests

class Spotify:
    def __init__(self, token):
        self.base_url = "https://api.spotify.com/v1"
        self.access_token = ""
        self.token = token

    def current_user(self):
        url = f"{self.base_url}/me"

        response = requests.get(url,
        headers={"Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.token)})
        
        response_json = response.json()
        return response_json

    def currently_playing(self):
        url = f"{self.base_url}/me/player/currently-playing"

        response = requests.get(url,
        headers={"Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.token)})
        
        response_json = response.json()
        return response_json