from selenium import webdriver
import time

class Selenium():
    url_baidu = "https:baidu.com"
    url_jd = "https:jd.com"
    url_tianMao = "https:tmall.com"

    def __init__(self, text):
        super().__init__()
        self.initWebDriver(text)
    def initWebDriver(self, text):

        if text == "Chrome":
            self.driver = webdriver.Chrome()

    def setSearchTarget(self, text):
        self.url = ""
        if text == "Baidu":
            self.url = self.url_baidu
        elif text == "JD":
            self.url = self.url_jd
        elif text == "TianMao":
            self.url = self.url_tianMao
        self.driver.get(self.url)
    def search(self, searchText):
        if self.url == self.url_baidu:
            self.searchByBaidu(searchText)
        elif self.url == self.url_jd:
            self.searchByJd(searchText)
        elif self.url == self.url_tianMao:
            self.searchByTianMao(searchText)

    def searchByJd(self, searchText):
        searchForm = self.driver.find_element_by_id("key")
        searchForm.clear()
        searchForm.send_keys(searchText)
        searchForm.submit()

    def searchByBaidu(self, searchText):
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys(searchText)
        self.driver.find_element_by_id("su").click()

    def searchByTianMao(self, searchText):
        searchForm =self.driver.find_element_by_id("mq").clear()
        searchForm.send_keys(searchText)
        searchForm.submit()
