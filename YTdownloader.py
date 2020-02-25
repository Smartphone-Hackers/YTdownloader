import requests
from bs4 import BeautifulSoup
import os, hashlib

class YTdownloader:
    def __init__(self, url):
        bit_url = "https://bitdownloader.com/download?video="
        self.url = bit_url + url.replace(":", "%3A").replace("/", "%2F").replace("?", "%3F").replace("=", "%3D")
        r = requests.get(self.url).content
        self.soup = BeautifulSoup(r, "lxml")
        self.div = self.soup.find("div", {"class": "info col-md-6 col-sm-6 col-xs-12"}) #None

    def title(self):
        try:
            return self.div.find("span", {"class": "title"}).text
        except AttributeError:
            return "Fetching Error!"

    def thumnail(self):
        img = self.div.find("img")
        return img.get("src")

    def duration(self):
        return self.div.find("div", {"style": "font-size: 17px; "}).text

    def download(self):
        dlink = self.soup.find("a", {"download": str(self.title()) + ".mp4"}).get("href")
        r = requests.get(dlink).content
        os.chdir(r"C:\Users\Anandh\Desktop")
        f = open(str(self.title()) + ".mp4", "wb")
        f.write(r)
        return "Video Downloaded on {}".format(os.getcwd())
