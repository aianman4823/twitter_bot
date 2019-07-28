import twitter
import config
import random


def puttweet():
    auth = twitter.OAuth(
    consumer_key = config.CONSUMER_KEY,
    consumer_secret = config.CONSUMER_SECRET,
    token = config.ACCESS_TOKEN,
    token_secret = config.ACCESS_SECRET)

    t = twitter.Twitter(auth=auth)

    #ツイートのみ
    lists=[
        "Hello, World!",
           ]
    status="Hello,World." #投稿するツイート
    t.statuses.update(status=status) #Twitterに投稿

