#!/usr/bin/python3
"""Script queries the reddit API
   And returns a list of titles for a subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    Returns a list of titles for a subreddit
    Args:
        subreddit(str): name of subreddit
        hot_list(list): titles in subreddit
        count(int): index count of title
    """
    temp_list = []
    reddit = 'https://www.reddit.com'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) \
                    Gecko/20100101 Firefox/91.0'
        }
    response = requests.get('{}/r/{}/hot.json?after={}&limit=200'
                            .format(reddit, subreddit, after),
                            headers=header, allow_redirects=False)
    if response.status_code != 200:
        return None
    posts = response.json().get('data').get('children')
    _next = response.json().get('data').get('after')
    for post in posts:
        hot_list.append(post.get('data').get('title'))

    if _next is not None:
        temp_list.append(hot_list)
        recurse(subreddit, hot_list, _next)
    return hot_list
