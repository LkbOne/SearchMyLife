import json
import re
import threading

import requests
from PyQt5.QtCore import pyqtSignal, QThread
from selenium.webdriver.common.keys import Keys

from common.JSEngine import JSEngine
from result.DouBanResult import DoubanResult
from result.ShopResult import ShopResult, JDResult, TianMaoResult, TaoBaoResult
from result.TXResult import QQMusicResult, QQVideoResult
from service.SearchService import Search
from lxml import etree
url_google = "https://www.google.com"
url_youtube = "https://www.youtube.com"

class Station(QThread):
    data = pyqtSignal(object)
    def __init__(self, station_url=None):
        super().__init__()
        self.station_url = station_url
        self.type = 0
        self.mainType = 0

    def visitStation(self, driver):
        if driver is not None and self.station_url is not None:
            t = threading.Thread(target=self.visit, args=(driver, self.station_url), name='visit:' + str(self.station_url))
            t.start()
        # t.join()

    def visit(self, driver, url, more_than_one_window = False):
        if more_than_one_window:
            # open_windows_js = "window.open('" + url + "');"
            driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
            # handles = driver.window_handles
            # driver.switch_to.window(handles[len(handles) - 0])
            driver.get(url)

        else:
            driver.get(url)

    def search(self, driver, content):
        pass

    def visitChildStation(self, url, trace_type):
        if self.driver is not None and url is not None:
            t = threading.Thread(target=self.visitChild, args=(self.driver, url, trace_type), name='visit:' + str(url))
            t.start()

    def visitChild(self, driver, url, trace_type=1):
        driver.get(url)
        Search().addSearchInfo(self.content, url, self.type, self.mainType, trace_type)

class BaiDuStation(Station):
    def __init__(self):
        super().__init__("https:baidu.com")
        self.type = 3
        self.mainType = 1
    def search(self, driver, content):
        t = threading.Thread(target=self.search_operator, args=(driver, content), name='search:' + str(self.station_url))
        t.start()
        # t.join()

    def search_operator(self, driver, content):
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(content)
        driver.find_element_by_id("su").click()
        Search().addSearchInfo(content, self.station_url, 3, 1, 0)
class JDStation(Station):
    def __init__(self):
        super().__init__("https:jd.com")
        self.type = 6
        self.mainType = 1
        self.driver = None

    def search(self, driver = None, content = None, group = True):
        if content is not None:
            self.content = content
        if self.driver is not None and driver is not None:
            self.driver = driver
            return
        if self.driver is None and driver is not None:
            self.driver = driver
        url = "https://search.jd.com/Search?keyword=" + self.content + "&enc=utf-8"

        if group:
            self.visit(self.driver, url)
            Search().addSearchInfo(content, self.station_url, 6, 1, 0)
        else:
            self.visit(self.driver, url, True)
        page_source = self.driver.page_source
        # page_source.encoding = 'utf-8'
        html = etree.HTML(page_source)
        datas = html.xpath('//li[contains(@class,"gl-item")]')
        needData = []
        if datas is not None:
            for data in datas:
                jd = JDResult()
                jd.set_title(data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()') + data.xpath('div/div[@class="p-name p-name-type-2"]/a/i/text()'))
                jd.set_url(data.xpath('div/div[@class="p-name p-name-type-2"]/a/@href'))
                img = data.xpath('div/div[1]/a/img/@src')
                jd.set_img(img)
                if len(img) == 0:
                    break
                jd.set_price(data.xpath('div/div[2]/strong/em/text()') + data.xpath('div/div[2]/strong/i/text()'))
                jd.set_shop_name(data.xpath('div/div[5]/span/a/text()'))
                jd.set_shop_url(data.xpath('div/div[5]/span/a/@href'))
                jd.set_commit_num(data.xpath('div/div[4]/strong/a/text()'))
                jd.set_commit_url(data.xpath('div/div[4]/strong/a/@href'))
                needData.append(jd)
            if group:
                tmData = TianMaoStation().search(self.driver, self.content, False)
                self.data.emit([needData, tmData])
            else:
                return needData
        if group:
            self.data.emit(None)
        else:
            return None
    def run(self):
        self.search()


class TianMaoStation(Station):
    def __init__(self):
        super().__init__("https:tmall.com")
        self.type = 7
        self.mainType = 1
        self.driver = None

    def search(self, driver = None, content = None, group = True):
        if content is not None:
            self.content = content
        if self.driver is not None and driver is not None:
            self.driver = driver
            return
        if self.driver is None and driver is not None:
            self.driver = driver
        url = "https://list.tmall.com/search_product.htm?q=" + self.content
        self.visit(self.driver, url)

        if group:
            self.visit(self.driver, url)
            Search().addSearchInfo(content, self.station_url, 7, 1, 0)
        else:
            self.visit(self.driver, url, True)

        page_source = self.driver.page_source
        # page_source.encoding = 'utf-8'
        html = etree.HTML(page_source)
        datas = html.xpath('//div[contains(@class,"product-iWrap")]')
        needData = []
        if datas is not None:
            for data in datas:
                tm = TianMaoResult()
                tm.set_title(data.xpath('p[2]/a/@title'))
                tm.set_url(data.xpath('div[1]/a/@href'))
                tm.set_img(data.xpath('div[1]/a/img/@src'))
                tm.set_price(data.xpath('p[1]/em/@title'))
                tm.set_shop_name(data.xpath('div[3]/a/text()'))
                tm.set_shop_url(data.xpath('div[3]/a/@href'))
                tm.set_month_deal(data.xpath('p[3]/span[1]/em/text()')) #月成交
                tm.set_commit_num(data.xpath('p[3]/span[2]/a/text()'))
                tm.set_commit_url(data.xpath('p[3]/span[2]/a/@href'))
                needData.append(tm)
            if group:
                jdData = JDStation().search(self.driver, self.content, False)
                self.data.emit([needData, jdData])
            else:
                return needData
        if group:
            self.data.emit(None)
        else:
            return None

    def run(self):
        self.search()
class TaoBaoStation(Station):
    def __init__(self):
        super().__init__("https://www.taobao.com")
        self.type = 7
        self.mainType = 1

    def search(self, driver, content):
        t = threading.Thread(target=self.search_operator, args=(driver, content), name='search:' + str(self.station_url))
        t.start()
        # t.join()

    def search_operator(self, driver = None, content = None):
        if content is not None:
            self.content = content
        if driver is not None:
            self.driver = driver
            # return
        url = "https://s.taobao.com/search?q=" + self.content
        self.visit(self.driver, url)
        res = requests.get(url)
        Search().addSearchInfo(content, self.station_url, 7, 1, 0)
        page_source = self.driver.page_source
        html = etree.HTML(res.text)
        datas = html.xpath('//div[contains(@class,"item J_MouserOnverReq")]')
        needData = []
        for data in datas:
            tm = TaoBaoResult()
            tm.set_title(data.xpath('div[2]/div[2]/a/text()') + data.xpath('div[2]/div[2]/a/span/text()'))
            tm.set_url(data.xpath('div[1]/div/div[1]/a/@href'))
            tm.set_img(data.xpath('div[1]/div/div[1]/a/img/@src'))
            tm.set_price(data.xpath('div[2]/div[1]/div[1]/strong/text()'))
            tm.set_payed(data.xpath('div[2]/div[1]/div[2]/text()'))
            tm.set_shop_name(data.xpath('div[2]/div[3]/div[1]/a/span[2]/text()'))
            tm.set_shop_url(data.xpath('div[2]/div[3]/div[1]/a/@href'))
            tm.set_location(data.xpath('div[2]/div[3]/div[2]/text()'))
            needData.append(tm)
            self.data.emit([needData])


class TXStation(Station):
    def __init__(self, station_url=None):
        super().__init__(station_url)

class QQMusicStation(TXStation):
    def __init__(self, driver = None, content = None):
        super().__init__("https://y.qq.com/")
        self.driver = driver
        self.content = content
        self.type = 4
        self.mainType = 4
    def search(self, driver = None, content = None, group = True):

        if content is not None:
            self.content = content
        if driver is not None:
            self.driver = driver
            return

        if self.driver is None:
            self.data.emit(None)
        url = "https://y.qq.com/portal/search.html#t=song&page=1&w=" + self.content
        self.visit(self.driver, url)
        if group:
            Search().addSearchInfo(self.content, url, 4, 4, 0)

        songDataUrl = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=63736116447151401&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=" + self.content + "&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0"
        songDataResponse = requests.get(songDataUrl)
        songData = json.loads(songDataResponse.text)
        songList = songData['data']['song']['list']
        needSongData = []
        for song in songList:
            qqSong = QQMusicResult()
            qqSong.setSongTitle(song['title'])
            qqSong.setSubTitle(song['subtitle'])
            qqSong.setUrl(song['url'])
            qqSong.setId(song['id'])
            album = song['album']
            qqSong.setAlbumTitle(album['name'])
            singer = song['singer']
            qqSong.setSingerName(singer[0]['title'])
            needSongData.append(qqSong)
        if group:
            needData = DouBanMusicStation().search(self.driver, self.content, False)
            self.data.emit([needSongData, needData])
        else:
            return needSongData
        self.data.emit(None)
    def run(self):
        self.search()

class QQVideoStation(TXStation):
    def __init__(self, driver = None, content = None):
        super().__init__("https://v.qq.com/")
        self.driver = driver
        self.content = content
        self.type = 4
        self.mainType = 3

    def search(self, driver = None, content = None, group = True):

        if content is not None:
            self.content = content
        if driver is not None:
            self.driver = driver
            return

        url = "https://v.qq.com/x/search/?q=" + self.content
        self.visit(self.driver, url)
        responseVideo = requests.get(url)
        html = etree.HTML(responseVideo.text)
        # /html/body/div[2]/div[2]/div[1]
        # /html/body/div[2]/div[2]/div[1]/div[4]
        # /html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div/a
        # /html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div/a/img
        # /html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div/h2/a
        # /html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div/span
        # /html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/span[2]/a
        # /html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/span[2]
        datas = html.xpath('//div[contains(@class,"result_ite")]')
        needData = []
        for data in datas:
            qv = QQVideoResult()
            qv.setTitle(data.xpath('div[1]/div/h2/a/text()'))
            qv.setSubTitle(data.xpath('div[1]/div/div/div[1]/span[2]/text()'))
            qv.setUrl(data.xpath('div[1]/div/a/@href'))
            if len(qv.getUrl()) == 0:
                break
            qv.setImg(data.xpath('div[1]/div/a/img/@src'))
            qv.setScore(data.xpath('div[1]/div/span/text()'))
            if len(qv.getScore()) == 0:
                 break
            qv.setDirector(data.xpath('div[1]/div/div/div[2]/span[2]/a/text()'))
            qv.setDirectorUrl(data.xpath('div[1]/div/div/div[2]/span[2]/a/@href'))
            needData.append(qv)
        if len(needData) == 0:
            needData = None
        if group:
            dbVideo = DouBanVideoStation().search(self.driver, self.content, False)
            self.data.emit([needData, dbVideo])
        else:
            return needData

    def run(self):
        self.search()

class DouBanStation(Station):
    def __init__(self, station_url="https://www.douban.com/"):
        super().__init__(station_url)


class DouBanBookStation(DouBanStation):
    def __init__(self, driver = None, content = None):
        super().__init__("https://book.douban.com/")
        self.driver = driver
        self.content = content
        self.type = 5
        self.mainType = 2

    def search(self, driver = None, content = None, group = True):
        if content is not None:
            self.content = content
        if driver is not None:
            self.driver = driver
        url = 'https://book.douban.com/subject_search?search_text=' + self.content
        self.visit(self.driver, url)
        response = requests.get(url)
        encodedData = re.search('window.__DATA__ = "([^"]+)"', response.text).group(1)  # 加密的数据
        douBan = JSEngine().decodeDouban(encodedData)
        if douBan is not None:
            payload = douBan['payload']
            needData = []
            if payload is not None:
                for item in payload['items']:
                    book = DoubanResult.Book()
                    if 'rating'not in item:
                        continue
                    book.setRateInfo(item['rating'])
                    book.setId(item['id'])
                    book.setTitle(item['title'])
                    book.setUrl(item['url'])
                    book.setActor(item['abstract'])
                    book.setCover(item['cover_url'])
                    book.setDescr(item['abstract_2'])
                    needData.append(book)
                if group:
                    jdData = JDStation().search(self.driver, self.content, False)
                    tmData = TianMaoStation().search(self.driver, self.content, False)
                    self.data.emit([jdData, needData, tmData])
                else:
                    return needData
        if group:
            self.data.emit(None)
        else:
            return None



    def run(self):
        self.search()
class DouBanVideoStation(DouBanStation):
    def __init__(self):
        super().__init__("https://movie.douban.com")
        self.driver = None

    def search(self, driver = None, content = None, group = True):
        if content is not None:
            self.content = content
        if driver is not None:
            self.driver = driver

        response = requests.get('https://movie.douban.com/subject_search?search_text=' + self.content)
        encodedData = re.search('window.__DATA__ = "([^"]+)"', response.text).group(1)  # 加密的数据
        douBan = JSEngine().decodeDouban(encodedData)
        if douBan is not None:
            payload = douBan['payload']
            needData = []
            if payload is not None:
                for item in payload['items']:
                    video = DoubanResult.Video()
                    video.setId(item['id'])
                    video.setTitle(item['title'])
                    video.setUrl(item['url'])
                    video.setActor(item['abstract_2'])
                    video.setCover(item['cover_url'])
                    video.setDescr(item['abstract'])
                    video.setRateInfo(item['rating'])
                    needData.append(video)
                if group:
                    self.data.emit([needData])
                else:
                    return needData
        if group:
            self.data.emit(None)
        else:
            return None

class DouBanMusicStation(DouBanStation):
    def __init__(self):
        super().__init__("https://music.douban.com")
        self.driver = None

    def search(self, driver = None, content = None, group = True):
        if content is not None:
            self.content = content
        if driver is not None:
            self.driver = driver

        response = requests.get('https://music.douban.com/subject_search?search_text=' + self.content)
        encodedData = re.search('window.__DATA__ = "([^"]+)"', response.text).group(1)  # 加密的数据
        douBan = JSEngine().decodeDouban(encodedData)
        if douBan is not None:
            payload = douBan['payload']
            needData = []
            if payload is not None:
                for item in payload['items']:
                    music = DoubanResult.Music()
                    music.setId(item['id'])
                    music.setTitle(item['title'])
                    music.setUrl(item['url'])
                    music.setActor(item['abstract'])
                    music.setCover(item['cover_url'])
                    music.setDescr(item['abstract_2'])
                    needData.append(music)
            if group:
                self.data.emit([needData])
            else:
                return needData
        if group:
            self.data.emit(None)
        else:
            return None

    def run(self):
        self.search()