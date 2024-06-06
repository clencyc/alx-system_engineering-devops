#!/usr/bin/python3
"""
Function to query the Reddit API and return the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    return response.json().get("data").get("subscribers")
