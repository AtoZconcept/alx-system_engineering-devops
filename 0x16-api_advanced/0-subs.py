#!/usr/bin/python3
"""Module to query the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """defined function that return number of subscribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    header = {'User-Agent': 'Mozilla/5.0 (Linux x86_64) Edge109.0'}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
