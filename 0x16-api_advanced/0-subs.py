#!/usr/bin/python3
"""Module to query the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """defined function that return number of subscribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    header = {'User-Agent': 'Custom User Agent'}
    try:
        response = requests.get(url, headers=header, allow_redirects=False)
        response.raise_for_status()
        return response.json().get('data').get('subscribers')
    except Exception:
        return 0
