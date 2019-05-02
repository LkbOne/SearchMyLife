from common.net import RequestBackend
import json
class Search():
    addr = "http://120.77.86.76:6060/"
    local = "search/"

    def addSearchInfo(self, content, url, type, mainType, traceType):

        visit = "addSearchInfo"
        inter = self.addr + self.local + visit
        param = {
            "content": content,
            "url": url,
            "type": type,
            "mainType": mainType,
            "traceType": traceType
        }
        resp = RequestBackend().postRequest(inter, param)
        res = json.loads(resp.data)

    def addBatchSearchInfo(self, urls, id):
        print("id:"+str(id))
        visit = "addBatchSearchInfo"
        inter = self.addr + self.local + visit
        param = {
            "urls": urls,
            "uid": id
        }
        resp = RequestBackend().postRequest(inter, param)
        res = json.loads(resp.data)
        return res

    def search(self, type, searchContent):
        call = RequestBackend()
        addr = "http://120.77.86.76:6060/"
        local = "search/"
        visit = "search"

        url = addr + local + visit
        print("type:" + str(type)+ "\\n")
        print("searchContent:" + str(searchContent) + "\\n")
        param = {
            'searchContent': searchContent,
            'type':type
        }
        resp = call.postRequest(url,param)
        res = json.loads(resp.data)
        resTemp = res['data']["result"]
        return resTemp

    def rebackUrl(self, crawlerUrl):
        call = RequestBackend()
        addr = "http://localhost:7070/"
        local = "search/"
        visit = "crawler"
        url = addr + local + visit
        param = {
            'url': crawlerUrl
        }
        call.postRequest(url, param)
