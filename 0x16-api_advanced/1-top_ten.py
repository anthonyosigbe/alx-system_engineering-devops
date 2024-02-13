#!/usr/bin/python3
import requests


def top_ten(subreddit):
    # Define the URL for the Reddit API request
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    # Set custom User-Agent header to comply with Reddit's API rules
    headers = {'User-Agent': '0x16-api_advanced:subreddit.hot.titles:v1.0 (by /u/anthonyosigbe)'}
    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers)
        # Check if the subreddit is valid (status code 200) and not redirected
        if response.status_code == 200 and response.url == url:
            data = response.json()
            # Extract the list of posts
            posts = data.get('data', {}).get('children', [])
            if posts:
                # Print the title of each post
                for post in posts:
                    print(post['data']['title'])
            else:
                # If there are no posts, print None
                print(None)
        else:
            # If the subreddit is not valid, print None
            print(None)
    except requests.RequestException:
        # Handle exceptions for the requests call
        print(None)
