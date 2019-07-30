import tweepy

import random
import os
#xxxxxxxxxxxxxxxxxxxxxは各自取得したAPIをkeyを入れてください。

def liketweet():
    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    ACCESS_SECRET = os.environ["ACCESS_SECRET"]
    # インスタンス作成
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    search_words = ["プログラミング","エンジニア","プログラマー","フリーランス"]
    q = search_words[random.randrange(len(search_words))]
    # ここで検索をかけています。
    # 検索したいワードをqという変数に入れます。今回は"プログラミング"でやってます。
    # 取得したいTweet数をcountという変数に入れます。今回は100でやってます。
    search_results = api.search(q=q, count=100)
    for result in search_results:
        tweet_id = result.id #Tweetのidを取得
        user_id = result.user._json['id'] #ユーザーのidを取得
        try:
            api.create_favorite(tweet_id) #ファボする
            api.create_friendship(user_id) #フォローする
        except Exception as e:
            print(e)