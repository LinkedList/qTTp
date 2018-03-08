import requests
from datetime import date


class Req(object):
    def __init__(self, method, protocol, url, headers, body, rawFile):
        super(Req, self).__init__()
        self.method = method
        self.protocol = protocol
        self.url = url
        self.headers = headers
        self.date = date.today()
        self.body = body
        self.file = rawFile

    def buildUrl(self):
        return self.protocol + "://" + self.url

    def buildTextRepresentation(self):
        return self.method + " " + self.url

    def isBinary(self):
        return self.file

    def buildRequestAndCall(self):
        data = self.buildDataObj()

        return requests.request(
            method=self.method,
            url=self.buildUrl(),
            headers=self.headers,
            data=data)

    def buildDataObj(self):
        if self.isBinary():
            data = open(self.file, 'rb').read()
        elif type(self.body) == dict:
            activeData = {k: v for k, v in self.body.items() if v['active'] == True}
            data = {}
            for k, v in activeData.items():
                data[k] = v['value']
        else:
            data = self.body
        return data

