#!/usr/bin/python3
"""Script queries the subreddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    Gets the number of subcribers to a subreddit
    Args:
        subreddit: name of subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) \
                Gecko/20100101 Firefox/91.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
