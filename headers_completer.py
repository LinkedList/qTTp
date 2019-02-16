from PySide2.QtCore import Qt
from PySide2.QtWidgets import QStyledItemDelegate, QLineEdit, QCompleter


class HeadersCompleter(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(HeadersCompleter, self).__init__(parent)

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        self._completerSetupFunction(editor, index)
        return editor

    def _completerSetupFunction(self, editor, index):
        completer = QCompleter(getHeadersData(), editor)
        completer.setCompletionColumn(0)
        completer.setCompletionRole(Qt.EditRole)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        try:
            editor.setCompleter(completer)
        except:
            pass


def getHeadersData():
    return [
        "Accept",
        "Accept-Charset",
        "Accept-Encoding",
        "Accept-Language",
        "Accept-Ranges",
        "Access-Control-Allow-Credentials",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Methods",
        "Access-Control-Allow-Origin",
        "Access-Control-Expose-Headers",
        "Access-Control-Max-Age",
        "Access-Control-Request-Headers",
        "Access-Control-Request-Method",
        "Age",
        "Allow",
        "Authorization",
        "Cache-Control",
        "Connection",
        "Content-Encoding",
        "Content-Disposition",
        "Content-Language",
        "Content-Length",
        "Content-Location",
        "Content-Range",
        "Content-Type",
        "Cookie",
        "Date",
        "ETag",
        "Expect",
        "Expires",
        "From",
        "Host",
        "If-Match",
        "If-Modified-Since",
        "If-None-Match",
        "If-Range",
        "If-Unmodified-Since",
        "Last-Modified",
        "Link",
        "Location",
        "Max-Forwards",
        "Origin",
        "Pragma",
        "Proxy-Authenticate",
        "Proxy-Authorization",
        "Range",
        "Referer",
        "Retry-After",
        "Server",
        "Set-Cookie",
        "Set-Cookie2",
        "TE",
        "Trailer",
        "Transfer-Encoding",
        "Upgrade",
        "User-Agent",
        "Vary",
        "Via",
        "Warning",
        "WWW-Authenticate"
    ]
