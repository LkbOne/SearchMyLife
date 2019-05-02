class DoubanResult(object):

    class Music(object):
        id = ""
        title = ""
        url = ""
        actor = ""
        cover = ""
        descr = ""
        def setId(self, id):
            self.id = id
        def setTitle(self, title):
            self.title = title
        def setUrl(self, url):
            self.url = url
        def setActor(self, actor):
            self.actor = actor
        def setCover(self, cover):
            self.cover = cover
        def setDescr(self, descr):
            self.descr = descr

        def getId(self):
            return self.id
        def getTitle(self):
            return self.title
        def getUrl(self):
            return self.url
        def getActor(self):
            return self.actor
        def getCover(self):
            return self.cover
        def getDescr(self, ):
            return self.descr


    class Video(object):
        id = ""
        title = ""
        url = ""
        actor = ""
        cover = ""
        descr = ""
        rateInfo = ""

        def setId(self, id):
            self.id = id
        def setTitle(self, title):
            self.title = title
        def setUrl(self, url):
            self.url = url
        def setActor(self, actor):
            self.actor = actor
        def setCover(self, cover):
            self.cover = cover
        def setDescr(self, descr):
            self.descr = descr
        def setRateInfo(self, rateInfo):
            self.rateInfo = rateInfo

        def getId(self):
            return self.id
        def getTitle(self):
            return self.title
        def getUrl(self):
            return self.url
        def getActor(self):
            return self.actor
        def getCover(self):
            return self.cover
        def getDescr(self):
            return self.descr
        def getRateInfo(self):
            return self.rateInfo

    class Book(object):
        id = ""
        title = ""
        url = ""
        actor = ""
        cover = ""
        descr = ""
        rateInfo = ""

        def setId(self, id):
            self.id = id
        def setTitle(self, title):
            self.title = title
        def setUrl(self, url):
            self.url = url
        def setActor(self, actor):
            self.actor = actor
        def setCover(self, cover):
            self.cover = cover
        def setDescr(self, descr):
            self.descr = descr
        def setRateInfo(self, rateInfo):
            self.rateInfo = rateInfo

        def getId(self):
            return self.id
        def getTitle(self):
            return self.title
        def getUrl(self):
            return self.url
        def getActor(self):
            return self.actor
        def getCover(self):
            return self.cover
        def getDescr(self):
            return self.descr
        def getRateInfo(self):
            return self.rateInfo