class QQMusicResult():
    songTitle = None
    url = None
    id = None
    albumTitle = None
    singerName = None
    subTitle = None

    def setSongTitle(self, songTitle):
        self.songTitle = songTitle

    def setUrl(self, url):
        self.url = url

    def setId(self, id):
        self.id = id

    def setAlbumTitle(self, albumTitle):
        self.albumTitle = albumTitle

    def setSingerName(self, singerName):
        self.singerName = singerName

    def setSubTitle(self, subTitle):
        self.subTitle = subTitle

    def getSongTitle(self):
        return self.songTitle

    def getUrl(self):
        return self.url

    def getId(self):
        return self.id

    def getAlbumTitle(self):
        return self.albumTitle

    def getSingerName(self):
        return self.singerName

    def getSubTitle(self):
        return self.subTitle
