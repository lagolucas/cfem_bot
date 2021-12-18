import tweepy
from json import load


def autentica():
    with open("config.json") as jsonfile:
        config = load(jsonfile)['twitter-keys']

    api = tweepy.Client(consumer_key=config['api_key'], consumer_secret=config['api_secret_key'], 
            access_token=config['access_token'], access_token_secret=config['access_token_secret'],
            wait_on_rate_limit=True)

    return api