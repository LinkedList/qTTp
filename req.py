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
