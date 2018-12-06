from selenium import webdriver
import time

class Selenium():
    url_baidu = "https:baidu.com"
    url_jd = "https:jd.com"
    url_tianMao = "https:tmall.com"
    url_google = "https://www.google.com"
    url_youtube = "https://www.youtube.com"
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
        elif text == "Google":
            self.url = self.url_google
        elif text == "Youtube":
            self.url = self.url_youtube
        self.driver.get(self.url)
    def search(self, searchText):
        if self.url == self.url_baidu:
            self.searchByBaidu(searchText)
        elif self.url == self.url_jd:
            self.searchByJd(searchText)
        elif self.url == self.url_tianMao:
            self.searchByTianMao(searchText)
        elif self.url == self.url_google:
            self.searchByGoogle(searchText)
        elif self.url == self.url_youtube:
            self.searchByYoutube(searchText)

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
    def searchByYoutube(self, searchText):
        searchInput = self.driver.find_element_by_xpath(".//input[@id='search']")
        searchInput.clear()
        searchInput.send_keys(searchText)
        searchInput.submit()


