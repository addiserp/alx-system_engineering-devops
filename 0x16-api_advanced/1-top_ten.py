#!/usr/bin/python3
"""
    a function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
        will display top 10 hottest posts on a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    options = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=options,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    rsult = response.json().get("data")
    [print(c.get("data").get("title")) for c in rsult.get("children")]
