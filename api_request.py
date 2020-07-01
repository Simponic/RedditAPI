from bs4 import BeautifulSoup
from flask_restful import Api, Resource, reqparse
from post import Post
import requests

class APIRequest(Resource):
    def get(self, subreddit="popular", numPosts=10, show_ads=0, show_stickied=1):
        """Get data"""
        url = "https://old.reddit.com/r/" + subreddit
        headers = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(url, headers=headers)
        reddit_soup = BeautifulSoup(page.text, "html.parser")
        posts = reddit_soup.find_all("div", class_="thing")
        post_arr = {"data": []}
        for i in range(numPosts):
            try:
                post_data = Post(posts[i])
                if (post_data.isAd and not show_ads):
                    i -= 1
                elif (post_data.isStickied and not show_stickied):
                    i -= 1
                else:
                    post_arr["data"].append(Post(posts[i]).getJSON())
            except:
                return {"data": "Not found"}, 404
        return post_arr, 200

if __name__ == "__main__":
    testAPIR = APIRequest
