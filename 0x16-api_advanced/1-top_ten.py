#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "anthonyosigbe"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url,
            headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        results = response.json().get("data", {}).get("children", [])
        for child in results:
            title = child.get("data", {}).get("title")
            if title:
                print(title)
    except ValueError:
        print("Error decoding JSON")
