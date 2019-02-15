import requests

class HttpClient:
    def __init__(self, timeout=0.3):
        """Timeout is in seconds
        http://docs.python-requests.org/en/master/user/quickstart/#timeouts
        """
        self.timeout = timeout

    def get(self, url, params=None, timeout=None):
        return requests.get(url, params, timeout=[timeout if timeout else self.timeout])

    def post(self, url, data=None, json=None, timeout=None):
        return requests.post(url, data, json, timeout=[timeout if timeout else self.timeout])
