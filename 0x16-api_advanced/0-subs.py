#!/usr/bin/python3
"""Fetches subreddit subscriber count."""

import requests


def number_of_subscribers(subreddit):
    """Returns subscriber count for a specified subreddit or
    0 if subreddit is invalid."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.ok:
        return response.json().get("data", {}).get("subscribers", 0)
    return 0
