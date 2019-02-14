from datetime import datetime

from app.Core.Token import Token

valid_refresh_token = "Refresh Token"
refreshed_token = "Refreshed Token"

def fake_refresh_method(token):
    return refreshed_token, datetime.utcnow() if token == valid_refresh_token else ""

def test_when_expired_get_should_get_valid_token():
    t = Token(fake_refresh_method, valid_refresh_token)
    token = t.get()
    assert token == refreshed_token