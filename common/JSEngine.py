import execjs

class JSEngine():
    def __init__(self):
        super().__init__()
        with open('static/decodeDouBan.js', 'r') as f:
             decrypt_js = f.read()
        self.ctx = execjs.compile(decrypt_js)

    def decodeDouban(self, encodedData):
        if encodedData is not None:
            return self.ctx.call('decrypt', encodedData)
        return None