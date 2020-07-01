from flask import Flask
from flask_restful import Api, Resource, reqparse
from bs4 import BeautifulSoup
from post import Post
from api_request import APIRequest
import requests

app = Flask(__name__)

api = Api(app)

api.add_resource(APIRequest, "/posts", "/posts/", "/posts/<string:subreddit>", "/posts/<string:subreddit>/<int:numPosts>", "/posts/<string:subreddit>/<int:numPosts>", "/posts/<string:subreddit>/<int:numPosts>/<int:show_ads>", "/posts/<string:subreddit>/<int:numPosts>/<int:show_ads>/<int:show_stickied>") 

if __name__ == "__main__":
    app.run(debug=False)
