import pytest

from datetime import datetime

from app.Core.Token import Token

class TokenTest:
    def test_when_expired_get_should_get_valid_token(self):
        t = Token(self.fake_refresh_method, self.valid_refresh_token())
        token = t.get()
        assert token == self.refreshed_token()

    # Helpers
    def valid_refresh_token(self):
        return "Refresh Token"
    
    def refreshed_token(self):
        return "Refreshed Token"

    def fake_refresh_method(self, token):
        return self.refreshed_token(), datetime.utcnow() if token == self.valid_refresh_token() else ""