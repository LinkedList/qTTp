from pprint import pprint
from jinja2 import Template
import requests
from datetime import date
from requests_toolbelt.multipart.encoder import MultipartEncoder


class Req(object):
    def __init__(self, method, protocol, url, headers, body, rawFile, context):
        super(Req, self).__init__()
        self.method = method
        self.protocol = protocol
        self.url = url
        self.headers = headers
        self.date = date.today()
        self.body = body
        self.file = rawFile
        self.context = context

    def isFormData(self):
        return 'Content-Type' in self.headers and self.headers['Content-Type'] == "multipart/form-data"

    def buildUrl(self):
        return self.transform(self.protocol + "://" + self.url)

    def buildTextRepresentation(self):
        return self.method + " " + self.url

    def isBinary(self):
        return self.file

    def buildRequestAndCall(self):
        data = self.buildDataObj()
        if self.isFormData():
            data = self.dataToMultipart(data)
            self.headers['Content-Type'] = data.content_type

        pprint(vars(self))
        pprint(data)
        return requests.request(
            method=self.method,
            url=self.buildUrl(),
            headers=self.headers,
            data=data)

    def dataToMultipart(self, data):
        return MultipartEncoder(fields = data)

    def buildDataObj(self):
        if self.isBinary():
            data = open(self.transform(self.file), 'rb').read()
        elif type(self.body) == dict:
            activeData = {k: v for k, v in self.body.items() if v['active'] == True}
            data = {}
            for k, v in activeData.items():
                data[k] = v['value']
        else:
            data = self.body
        return data

    def transform(self, what):
        template = Template(what)
        rendered = template.render(self.context)
        return rendered
