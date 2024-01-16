#!/usr/bin/python3
"""
    a recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If
    no results are found for the given subreddit, the function should
    return None.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
        will display a list of titles of all hot posts on a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    options = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=options,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    result = response.json().get("data")
    after = result.get("after")
    count += result.get("dist")
    for c in result.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
