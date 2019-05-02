import os
import sqlite3

from PyQt5.QtCore import pyqtSignal, QThread

from service.SearchService import Search


class urls(object):
    id = None
    url = None
    title = None
    visit_count = 0
    typed_count = 0
    last_visit_time = 0
    hidden = 0

def parse(url):
    try:
        parsed_url_components = url.split('//')
        sublevel_split = parsed_url_components[1].split('/',1)
        domian = sublevel_split[0].replace('www.','')
        return domian
    except IndexError:
        print('URL format error!!')

class UploadChromeHistory(QThread):
    data = pyqtSignal(object)
    def __init__(self, db_file, id):
        super().__init__()
        self._db_file = db_file
        self.id = id
    def upload_chrome_url_history(self):
        #指到用户的谷歌浏览器的历史记录
        if not self._db_file:
            self.data.emit(self._db_file)
        #查询数据库内容
        conn = sqlite3.connect(self._db_file)
        cursor = conn.cursor()
        select_statement_query = 'SELECT * FROM urls'
        cursor.execute(select_statement_query)
        results = cursor.fetchall()
        urls_list = []
        for id, url, title, visit_count, typed_count,last_visit_time, hidden in results:
            url_a = {}
            url_a['id'] = id
            url_a['url'] = url
            url_a['title'] = title
            url_a['visit_count'] = visit_count
            url_a['typed_count'] = typed_count
            url_a['last_visit_time'] = last_visit_time
            url_a['hidden'] = hidden
            urls_list.append(url_a)

        res = Search().addBatchSearchInfo(urls_list, self.id)
        print("res:%s",res)
        self.data.emit(res)
        return res
    def run(self):
        self.upload_chrome_url_history()


