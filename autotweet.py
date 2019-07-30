import twitter

import random
import os


def puttweet():
    auth = twitter.OAuth(
    consumer_key = os.environ["CONSUMER_KEY"],
    consumer_secret = os.environ["CONSUMER_SECRET"],
    token = os.environ["ACCESS_TOKEN"],
    token_secret = os.environ["ACCESS_SECRET"])

    t = twitter.Twitter(auth=auth)

    #ツイートのみ
    lists=[
        "Hello, World!",
           ]
    status="Hello,World." #投稿するツイート
    t.statuses.update(status=status) #Twitterに投稿

