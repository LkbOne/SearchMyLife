class ShopResult(object):

    def set_url(self, url):
        self.url = url

    def get_url(self):
        if self.url is None:
            return ""
        else:
            return self.url[0]

    def set_price(self, price):
        self.price = price

    def get_price(self):
        if self.price is None:
            return "--"
        else:
            return self.price[0]

    def set_img(self, img):
        self.img = img

    def get_img(self):
        if self.img is None:
            return ""
        else:
            return 'http:' + self.img[0]

    def set_title(self, title):
        self.title = title

    def get_title(self):
        if self.title is None:
            return ""
        else:
            return self.title[0]

    def set_commit_num(self, commit_num):
        self.commit_num = commit_num

    def set_commit_url(self, commit_url):
        self.commit_url = commit_url

    def set_shop_url(self, shop_url):
        self.shop_url = shop_url

    def set_shop_name(self, shop_name):
        self.shop_name = shop_name

class JDResult(ShopResult):
    def get_title(self):
        if self.title is None:
            return ""
        else:
            title = ""
            i = 0
            for part in self.title:
                if i != 0:
                    title += " "
                title += part
                i = 1
            return title
    def get_price(self):
        if self.price is None:
            return "--"
        else:
            return self.price[0] + self.price[1]
    pass

class TianMaoResult(ShopResult):
    def set_month_deal(self, month_deal):
        self.month_deal = month_deal
    pass

class TaoBaoResult(ShopResult):
    def set_payed(self, payed):
        self.payed = payed

    def set_location(self, location):
        self.location = location

