from datetime import datetime, timedelta
import json
import requests

from app.Core.HttpClient import HttpClient


class Client:
    auth_base_url = "https://api.imgur.com/oauth2/token"

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.http_client = HttpClient()

    def refresh_method(self, refresh_token):
        """Use a refresh token to get a new access token from the api and return it"""
        # Setup params
        params = {
                'refresh_token': refresh_token,
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'grant_type': 'refresh_token'}

        def get_access_token(params):
            request = self.http_client.post(self.auth_base_url, data=params)
            if request.ok:
                json_content = request.json()
                return json_content["access_token"], datetime.utcnow() + timedelta(seconds=json_content["expires_in"])
            else:
                return "", datetime.utcnow()

        return get_access_token(params)
