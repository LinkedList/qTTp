import json
from response_tabs import Ui_ResponseTabs
from PyQt5.QtWidgets import QTabWidget

class ResponseTabsWidget(QTabWidget, Ui_ResponseTabs):
    def __init__(self):
        super(ResponseTabsWidget, self).__init__()
        self.setupUi(self)

    def setHeaders(self, headers):
        headersText = ""
        for key in sorted(headers):
            headersText += "<b>" + key + "</b>" + ": " + headers[key] + "<br />"
        self.headersText.setHtml(headersText)

    def setResponseBody(self, response):
        if 'application/json' in response.headers['content-type']:
            body = self.parseJson(response)
            self.responseText.setHtml(body)
        else:
            body = response.text
            self.responseText.setPlainText(body)

    @staticmethod
    def parseJson(response):
        try:
            response.json()
            j = response.text
            parse = json.loads(j)
            dump = json.dumps(obj=parse, indent=4).replace(" ", "&nbsp;").replace("\n", "<br />")
            return dump
        except ValueError:
            return ""
