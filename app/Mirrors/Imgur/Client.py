from datetime import datetime, timedelta
import json
import requests

from app.Core.HttpClient import HttpClient

class Client:
    auth_base_url = "https://api.imgur.com/oauth2/token"

    def __init__(self, client_id, client_secret, http_client):
        self.client_id = client_id
        self.client_secret = client_secret
        self.http_client = http_client

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
                access_token, expiry_time = json_content["access_token"], datetime.utcnow() + timedelta(seconds=json_content["expires_in"]-300)
                return access_token, expiry_time
            else:
                return "", datetime.utcnow()

        return get_access_token(params)

    def get_refresh_token_request_url(self, response_type="POST", application_state=""):
        """Generates the url necessary for a user to use to get refresh tokens
        https://api.imgur.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&response_type=REQUESTED_RESPONSE_TYPE&state=APPLICATION_STATE
        """
        return self.auth_base_url + "/authorize?client_id={cid}&response_type={resp}&state={app_state}".format(
                    cid=self.client_id,
                    resp=response_type,
                    app_state=application_state
                )
