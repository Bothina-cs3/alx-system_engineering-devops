#!/usr/bin/python3
"""Module for querying the Reddit API and printing the top 10 hot posts."""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the top 10 hot posts
    for the given subreddit.
    
    Args:
        subreddit (str): The subreddit to query.
    
    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    
    sub_info = requests.get(url, headers=headers, allow_redirects=False)
    
    if sub_info.status_code >= 300:
        print(None)
        return
    
    data = sub_info.json().get("data")
    
    if data is None:
        print(None)
        return
    
    children = data.get("children")
    
    if children is None:
        print(None)
        return
    
    for child in children:
        print(child.get("data", {}).get("title"))

