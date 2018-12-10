import urllib3
class RequestBackend():
    httpPool = urllib3.PoolManager()

    def postRequest(self, url, params):
        resp = self.httpPool.request("post", url, body = params)
        print("post:" +  str(resp.status))

    def getRequest(self, url):
        resp = self.httpPool.request("get", url)
        print("get:" + str(resp.status))

    def putRequest(self, url):
        resp = self.httpPool.request("put", url)
        print("put:" + resp.status)

    def deleteRequest(self, url):
        resp = self.httpPool.request("delete", url)
        print("delete:" + resp.status)