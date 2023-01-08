#!/usr/bin/python3
"""Script queries the reddit API
    Lists out the top ten post of a subreddit
"""

import requests


def top_ten(subreddit):
    """
    Gets the first ten hot posts a subreddit
    Args:
        subreddit: name of subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) \
                Gecko/20100101 Firefox/91.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        children = response.json()['data']['children'][:10]
        for child in children:
            print(child['data']['title'])
    else:
        print('None')
