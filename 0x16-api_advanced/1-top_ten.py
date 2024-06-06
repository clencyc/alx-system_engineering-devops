#!/usr/bin/python3

"""
function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get("data").get("children")
    for i in range(10):
        print(data[i].get("data").get("title"))