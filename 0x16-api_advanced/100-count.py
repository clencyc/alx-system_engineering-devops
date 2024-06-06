#!/usr/bin/python3
"""
function that queries the Reddit API, parses the title of all hot articles, 
and prints a sorted count of given keywords (case-insensitive, delimited by spaces. 
Javascript should count as javascript, but java should not).
"""

import requests

import requests
from collections import defaultdict

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = defaultdict(int)
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f'?after={after}'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()
    for post in data['data']['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            counts[word] += title.split().count(word.lower())
    after = data['data'].get('after')
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        print_counts(counts)

def print_counts(counts):
    sorted_counts = sorted([(k, v) for k, v in counts.items() if v > 0], key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f'{word}: {count}')