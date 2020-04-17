#!/usr/bin/python3
"""Takes in 3 strings and sends a
search request to the Twitter API.

Display only 5 results in the following format:

[<Tweet ID>] <Tweet text> by <Tweet owner name>
"""

from base64 import b64encode
from sys import argv
import requests


if __name__ == "__main__":
    consumer_keys = "{0}:{1}".format(argv[1], argv[2])
    bearer_token_url = "https://api.twitter.com/oauth2/token"
    b64_consumer_keys = b64encode(bytes(consumer_keys, encoding='utf-8'))
    bearer_headers = {
        'Authorization': "Basic {0}".format(b64_consumer_keys),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    bearer_res = requests.post(
        bearer_token_url,
        auth=(argv[1], argv[2]),
        data={'grant_type': 'client_credentials'},
        headers=bearer_headers
    ).json()

    if {'token_type', 'access_token'} <= bearer_res.keys():
        tw_res_url = "https://api.twitter.com/1.1/search/tweets.json"
        tw_headers = {
            'Authorization': "Bearer {0}".format(bearer_res['access_token'])
        }
        tw_params = {
            'q': argv[3],
            'count': '5',
            'result_type': 'recent'
        }

        tweets = requests.get(
            tw_res_url,
            params=tw_params,
            headers=tw_headers).json()

        for tweet in tweets['statuses']:
            print("[{id}] {text} by {owner}".format(
                id=tweet['id'], text=tweet['text'], owner=tweet['user']['name']
                ))
