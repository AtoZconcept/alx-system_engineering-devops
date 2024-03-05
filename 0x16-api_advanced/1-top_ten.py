#!/usr/bin/python3
import requests
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""


def top_ten(subreddit):
    """function to return first top ten posts"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    header = {'User-Agent': 'Mozilla/5.0 (Linux x86_64) Edge109.0'}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0