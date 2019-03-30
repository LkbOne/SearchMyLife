from common.net import RequestBackend
import json
class Search():
    addr = "http://localhost:7070/"
    local = "search/"

    def addSearchInfo(self, ):
        call = RequestBackend()
        visit = "addSearchInfo"
        url = self.addr + self.local + visit
        param = {

        }
        resp = call.postRequest(url, param)
        res = json.loads(resp.data)


    def search(self, type, searchContent):
        call = RequestBackend()
        addr = "http://localhost:7070/"
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
