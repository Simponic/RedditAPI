import requests
import time
from bs4 import BeautifulSoup

class Post(object):
    def __init__(self, postObject):
        """A class for storing data of a reddit post"""
        self.postObject = postObject
        self.subreddit = self.postObject["data-subreddit"]
        self._class = self.postObject["class"]
        self.isStickied = ("stickied" in self._class)
        self.isAd = ("promoted" in self._class)
        self.link = self.postObject["data-url"] 
        self.title = self.postObject.find("a", class_="title").text
        self.flair = self.getFlair()
        self.timestamp = ("None" if self.isAd else self.postObject.find("time")["title"])
        self.score = int(self.postObject["data-score"])
        self.domain = self.postObject["data-domain"]
        self.textContent = "None"
        #if (self.domain == "self." + self.subreddit): # Is a text-post
            #self.textContent = self.getPostText()

    def getFlair(self):
        """Get flair of post"""
        flair = self.postObject.find("span", class_="linkflairlabel")
        if (flair):
            return flair["title"]
        else:
            return "None"

    def getPostText(self):
        """Get text from post, assuming it's text-only and store to textContent"""
        time.sleep(1)
        url = "https://old.reddit.com" + self.link
        headers = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(url, headers=headers)
        contentSoup = BeautifulSoup(page.text, "html.parser")
        textContent = contentSoup.find("div", class_="md").prettify() # Get string of html of content
        return textContent

    def getJSON(self):
        """Get JSON of class, will be useful for API requests"""
        return {
            "class": self._class,
            "isStickied": self.isStickied,
            "isAd": self.isAd,
            "link": self.link,
            "title": self.title,
            "flair": self.flair,
            "time": self.timestamp,
            "score": self.score,
            "domain": self.domain,
            "textContent": self.textContent
        }

    def display(self):
        """Method to display information of a post"""
        print("Score: " + str(self.score))
        print("Title: " + self.title)
        print("Flair: " + self.flair)
        print("Time posted: " + self.timestamp)
        print("Content link: " + self.link)
        print("Domain posted to:" + self.domain)
        print("Text content: " + self.textContent)
        print("Is ad: " + str(self.isAd))
        print("Is stickied: " + str(self.isStickied))
