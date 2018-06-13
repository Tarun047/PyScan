from urllib.request import Request, urlopen,build_opener
from urllib.parse import urlencode
import json
import requests


class Connector:
    def __init__(self, k, r):
        self.url = 'https://www.virustotal.com/vtapi/v2/file/report'
        self.key = k
        self.res = r

    def getConnection(self):
        values = {'apikey': self.key, 'resource': self.res}
        data = urlencode(values)
        data = data.encode('ascii')
        self.req = Request(self.url, data)

    def getInfo(self):
        resp = urlopen(self.req).read()
        if resp != b'':
            return json.loads(resp.decode('utf-8'))
        else:
            return "Please Wait a Minute and Retry Again"


class Uploader:
    def __init__(self, k, r):
        self.url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        self.key = k
        self.res = r

    def initUpload(self):
        params = {'apikey': self.key}
        files = {'file': self.res}
        response = requests.post(self.url, files=files, params=params)
        return response.json()