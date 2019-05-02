class TXResult():
    title = None
    url = None
    subTitle = None
    img = None
    def setUrl(self, url):
        self.url = url
    def getUrl(self):
        return self.url
    def setTitle(self, title):
        self.title = title
    def getTitle(self):
        return self.title
    def setSubTitle(self, subTitle):
        self.subTitle = subTitle
    def getSubTitle(self):
        return self.subTitle
    def setImg(self, img):
        self.img = img
    def getImg(self):
        return self.img
class QQVideoResult(TXResult):
    score = 0
    director = None
    directorUrl = None
    def getUrl(self):
        if len(self.url) != 0:
            return self.url[0]
    def getTitle(self):
        show_title = ""
        for value in self.title:
            show_title += value
        return show_title
    def getSubTitle(self):
        show_title = ""
        for value in self.title:
            show_title += value
        return show_title
    def getImg(self):
        if len(self.img) != 0:
            return 'http:' + self.img[0]
    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def setDirector(self, director):
        self.director = director

    def getDirector(self):
        return self.director

    def setDirectorUrl(self, directorUrl):
        self.directorUrl = directorUrl

    def getDirectorUrl(self):
        return 'https://v.qq.com/x/search/?q=' + self.directorUrl

    pass
class QQMusicResult(TXResult):
    songTitle = None
    url = None
    id = None
    albumTitle = None
    singerName = None
    subTitle = None

    def setSongTitle(self, songTitle):
        self.songTitle = songTitle
    def setId(self, id):
        self.id = id

    def setAlbumTitle(self, albumTitle):
        self.albumTitle = albumTitle

    def setSingerName(self, singerName):
        self.singerName = singerName

    def getSongTitle(self):
        return self.songTitle


    def getId(self):
        return self.id

    def getAlbumTitle(self):
        return self.albumTitle

    def getSingerName(self):
        return self.singerName

