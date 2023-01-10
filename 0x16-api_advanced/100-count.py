#!/usr/bin/python3
"""Script queries the reddit API
   And returns a list of titles for a subreddit
"""

import requests


def count_words(subreddit, word_list, word_dict={}, after=''):
    """
    Returns a list of titles for a subreddit
    Args:
        subreddit(str): name of subreddit
        hot_list(list): titles in subreddit
        count(int): index count of title
    """
    reddit = 'https://www.reddit.com'
    header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) \
                    Gecko/20100101 Firefox/91.0'
        }
    response = requests.get('{}/r/{}/hot.json?after={}&limit=200'
                            .format(reddit, subreddit, after),
                            headers=header, allow_redirects=False)
    if response.status_code != 200:
        return None
    words = []
    for word in word_list:
        word = word.lower()
        words.append(word)
    for word in words:
        if word not in word_dict:
            word_dict[word] = 0
        else:
            word_dict[word] += 1

    hot_posts = response.json().get('data').get('children')
    _next = response.json().get('data').get('after')

    for post in hot_posts:
        title = post.get('data').get('title')
        title_list = title.lower().split(' ')
        for key, val in word_dict.items():
            if key in title_list:
                word_dict[key] = val + 1

    if _next is None:
        sort = sorted(word_dict, key=lambda x: x[1], reverse=True)
        for key in sort:
            print('{}: {}'.format(key, word_dict[key]))
    if _next:
        count_words(subreddit, word_list, word_dict, _next)
