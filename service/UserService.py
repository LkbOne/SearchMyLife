import json

from common.net import RequestBackend


class User():
    addr = "http://120.77.86.76:6060/"
    local = "user/"
    def Login(self, content, password, type):

        visit = "login"
        inter = self.addr + self.local + visit
        param = {
            "content": content,
            "password": password,
            "type": type
        }
        resp = RequestBackend().postRequest(inter, param)
        return json.loads(resp.data)

    def getCode(self, content):
        visit = "getVerificationCode"
        inter = self.addr + self.local + visit
        param = {
            "email": content,
        }
        resp = RequestBackend().postRequest(inter, param)
        return json.loads(resp.data)