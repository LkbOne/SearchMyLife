import urllib3
import json

class RequestBackend():
    httpPool = urllib3.PoolManager()

    def postRequest(self, url, params):
        headers = {'Content-Type': 'application/json'}
        resp = self.httpPool.request("post", url=url, headers=headers,body=json.dumps(params))
        # print("post:" + str(resp.data))
        return resp
    def getRequest(self, url):
        resp = self.httpPool.request("get", url)
        # res = json.loads(resp.data)
        # resTemp = res['data']["result"]
        # aa = resTemp[0]
        return resp
    def putRequest(self, url):
        resp = self.httpPool.request("put", url)
        print("put:" + resp.status)

    def deleteRequest(self, url):
        resp = self.httpPool.request("delete", url)
        print("delete:" + resp.status)