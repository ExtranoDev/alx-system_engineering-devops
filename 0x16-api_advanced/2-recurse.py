#!/usr/bin/python3
"""Script queries the reddit API
   And returns a list of titles for a subreddit
"""

import requests


def recurse(subreddit, hot_list=[], count=0):
    """
    Returns a list of titles for a subreddit
    Args:
        subreddit(str): name of subreddit
        hot_list(list): titles in subreddit
        count(int): index count of title
    """
    if hot_list == []:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) \
                    Gecko/20100101 Firefox/91.0'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            child = response.json()['data']['children']
            if child:
                temp = child.pop(0)
                hot_list.append(temp['data']['title'])
                subreddit = child
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None
    else:
        if subreddit == []:
            return hot_list
        else:
            temp = subreddit.pop(0)
            hot_list.append(temp['data']['title'])
            return recurse(subreddit, hot_list)
