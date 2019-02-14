from datetime import datetime

class Token:
    def __init__(self, refresh_method, refresh_token, access_token="", expiry_time=None):
        self.refresh_method = refresh_method
        self.refresh_token = refresh_token
        self.expiry_time = expiry_time
        self.access_token = access_token
    
    def get(self):
        if self.expiry_time and datetime.utcnow() <= self.expiry_time:
            self.access_token = self.refresh_method()
        return self.access_token