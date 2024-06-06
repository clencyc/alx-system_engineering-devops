#!/usr/bin/python3
"""
function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests

def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    data = response.json().get("data").get("children")
    for i in range(len(data)):
        hot_list.append(data[i].get("data").get("title"))
    after = response.json().get("data").get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list)
