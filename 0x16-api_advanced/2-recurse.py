#!/usr/bin/python3
import requests


def recurse(subreddit, after='', hot_list=[]):
    # Base URL for fetching hot articles from a subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=25'
    if after:
        url += f'&after={after}'

    headers = {'User-Agent': 'api_advanced-project'}
    # Make the request to the Reddit API
    response = requests.get(url, headers=headers)
    # Check if the subreddit is valid and not a redirect (status code 200)
    if response.status_code != 200:
        return None
    # Load the JSON response
    data = response.json()
    # Extract the list of articles
    articles = data.get('data', {}).get('children', [])
    if not articles:
        return hot_list if hot_list else None
    # Add the titles of the current page of articles to the hot_list
    hot_list.extend([article['data']['title'] for article in articles])
    # Check if there is a next page
    after = data.get('data', {}).get('after', '')
    if not after:
        return hot_list
    else:
        # Recursively call the function to get articles from the next page
        return recurse(subreddit, after, hot_list)
