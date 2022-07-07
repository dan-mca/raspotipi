from urllib.parse import urljoin
import requests

class Spotify:
    def __init__(self):
        self.access_token = ""

    def currently_playing(self, token):
        url = "https://api.spotify.com/v1/me/player/currently-playing"

        response = requests.get(url,
        headers={"Content-Type": "application/json",
                                         "Authorization": "Bearer {}".format(token)})
        
        response_json = response.json()
        return response_json