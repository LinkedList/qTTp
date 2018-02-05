class Req(object):
    def __init__(self, method, protocol, url, headers):
        super(Req, self).__init__()               
        self.method = method
        self.protocol = protocol
        self.url = url
        self.headers = headers

    def buildUrl(self):
        return self.protocol + "://" + self.url

    def buildTextRepresentation(self):
        return self.method + " " + self.url
