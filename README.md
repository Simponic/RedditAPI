# RedditAPI
My first RESTful API built in python. Make requests to get the top posts of any subreddit.

Requirements:
* Python 3
* flask
* flask-restful
* beautifulsoup-4

---

Usage:

```python3 main.py```

To run the server

---
API Usage

Do a GET request to where the server is running. 

The syntax is like so:

```http://127.0.0.1:5000/posts/<str: subreddit name>/<int: number of posts>/<int (1 or 0): show ads>/<int (1 or 0): show stickied>```

You may remove any value to use the default values, like so

```http://127.0.0.1:5000/posts/<subreddit name>```

This will use the default 10 posts, without showing ads, and showing stickied posts

