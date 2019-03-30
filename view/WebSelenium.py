import json

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from selenium import webdriver
import time
import requests
import re

from common.JSEngine import JSEngine
from result.DouBanResult import DoubanResult
from result.QQMusicResult import QQMusicResult


class Selenium(QtCore.QThread):
    _signal = pyqtSignal(str)


    url_baidu = "https:baidu.com"
    url_jd = "https:jd.com"
    url_tianMao = "https:tmall.com"
    url_google = "https://www.google.com"
    url_youtube = "https://www.youtube.com"
    url_qqMusic = "https://y.qq.com/"
    url_qqVideo = "https://v.qq.com/"
    url_douBan = "https://www.douban.com/"


    def __init__(self, text):
        super(Selenium, self).__init__()
        self.initWebDriver(text)
        self.url = self.url_baidu
        self.driver.get(self.url)
        self.jsEngine = JSEngine()
    def initWebDriver(self, text):
        if text == "Chrome":
            self.driver = webdriver.Chrome()

    def setSearchTarget(self, text, url):
        print("url:" + str(text))
        if text == "Baidu" and url is None:
            self.url = self.url_baidu
        elif text == "JD" and url is None:
            self.url = self.url_jd
        elif text == "TianMao" and url is None:
            self.url = self.url_tianMao
        elif text == "Google" and url is None:
            self.url = self.url_google
        elif text == "Youtube" and url is None:
            self.url = self.url_youtube
        elif text == "QQMusic" and url is None:
            self.url = self.url_qqMusic
        elif text == "QQVideo" and url is None:
            self.url = self.url_qqVideo
        elif text == "DouBan" and url is None:
            self.url = self.url_douBan

        if url is not None and text is not None:
            self.driver.get(url)
        if url is not None and text is None:
            self.driver.get(url)
        if text is not None and url is None:
            self.driver.get(self.url)

    def search(self, searchText):
        print("search url:" + self.url)
        if self.url == self.url_baidu:
            self.searchByBaidu(searchText)
        elif self.url == self.url_jd:
            self.searchByJd(searchText)
        elif self.url == self.url_tianMao:
            self.searchByTianMao(searchText)
        elif self.url == self.url_google:
            self.searchByGoogle(searchText)
        elif self.url == self.url_youtube:
            self.searchYoutube(searchText)
        elif self.url == self.url_qqMusic:
            return self.searchQQMusic(searchText)
        elif self.url == self.url_qqVideo:
            return self.searchQQVideo(searchText)
        elif self.url == self.url_douBan:
            self.searchDouBan(searchText)


    def searchByJd(self, searchText):
        searchForm = self.driver.find_element_by_id("key")
        searchForm.clear()
        searchForm.send_keys(searchText)
        headPage = self.driver.find_elements_by_xpath('//button[@clstag="h|keycount|head|search_c"]')
        if (len(headPage) != 0):
            headPage[0].click()
        else:
            childPage = self.driver.find_element_by_css_selector("[class='button cw-icon']")
            childPage.click()

    def searchByBaidu(self, searchText):
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys(searchText)
        self.driver.find_element_by_id("su").click()

    def searchByTianMao(self, searchText):
        self.driver.find_element_by_id("mq").clear()
        self.driver.find_element_by_id("mq").send_keys(searchText)
        aa = self.driver.find_element_by_xpath(".//button[@type='submit']")
        aa.click()
    def searchByGoogle(self, searchText):
        searchInput = self.driver.find_element_by_css_selector("[class='gLFyf gsfi']")
        if(searchInput == None):
            searchInput = self.driver.find_element_by_css_selector("[class='gLFyf']")
        searchInput.clear()
        searchInput.send_keys(searchText)
        searchInput.submit()
    def searchYoutube(self, searchText):
        searchInput = self.driver.find_element_by_xpath(".//input[@id='search']")
        searchInput.clear()
        searchInput.send_keys(searchText)
        searchInput.submit()

    def searchQQMusic(self, searchText):
        url = "https://y.qq.com/portal/search.html#t=song&page=1&w=" + searchText
        self.setSearchTarget(self.url, url)

        songDataUrl = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=63736116447151401&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=" + searchText + "&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0"

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

        response = requests.get('https://music.douban.com/subject_search?search_text=' + searchText)
        encodedData = re.search('window.__DATA__ = "([^"]+)"', response.text).group(1)  # 加密的数据
        data = self.jsEngine.decodeDouban(encodedData)
        if data is not None:
            payload = data['payload']
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
            return needData, needSongData
        return data, needSongData

    # searchInput = self.driver.find_element_by_css_selector("[class='search_input__input']")
        # print('text:' + str(searchInput.get_attribute("placeholder")))
        # # searchInput.clear()
        #
        # 不是form的问题
        # searchInput.send_keys(searchText)
        # button = self.driver.find_element_by_css_selector("[class='search_input__btn']")
        # button.click()

    def searchQQVideo(self, searchText):
        url = "https://v.qq.com/x/search/?q=" + searchText
        self.setSearchTarget(self.url, url)
        response = requests.get('https://movie.douban.com/subject_search?search_text=' + searchText)
        encodedData = re.search('window.__DATA__ = "([^"]+)"', response.text).group(1)  # 加密的数据
        data = self.jsEngine.decodeDouban(encodedData)
        if data is not None:
            payload = data['payload']
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
            return needData
        return data
    def searchDouBan(self, searchText):
        # https://www.douban.com/search?q=aaa
        url = "https://www.douban.com/search?q=" + searchText
        self.setSearchTarget(self.url, url)
