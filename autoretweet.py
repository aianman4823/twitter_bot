import tweepy

import os
#xxxxxxxxxxxxxxxxxxxxxは各自取得したAPIをkeyを入れてください。

CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]
# インスタンス作成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

search_results = api.search(q="プログラミング", count=100)

for result in search_results:
    tweet_id = result.id
    user_id = result.user._json['id']  # ←追記
    try:
        api.create_favorite(tweet_id)
        api.retweet(tweet_id)          # ←追記
        # api.create_friendship(user_id) # ←追記
    except Exception as e:
        print(e)