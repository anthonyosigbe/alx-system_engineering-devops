#!/usr/bin/python3
"""
Module to fetch and print the titles of the top
10 hot posts of a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:reddit_api:v1.0.0 (by /u/anthonyosigbe)"}
    params = {"limit": 10}
    res = requests.get(url, headers=headers, params=params,
            allow_redirects=False)

    if res.status_code == 200:
        data = res.json().get("data", {}).get("children", [])
        for post in data:
            print(post.get("data", {}).get("title"))
    else:
        print("None")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
