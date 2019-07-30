import tweepy
import random
import os
#xxxxxxxxxxxxxxxxxxxxxは各自取得したAPIをkeyを入れてください。
def remove():
    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    ACCESS_SECRET = os.environ["ACCESS_SECRET"]
    # インスタンス作成
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    user_id="@CryptogramDo"
    # ここで検索をかけています。
    followers_id=api.followers_ids(user_id)
    following_id=api.friends_ids(user_id)

    lists=[100,200,300,400]

    for following in following_id:
        if following not in followers_id:
            userfollowers=api.get_user(following).followers_count
            if userfollowers < lists[random.randrange(len(lists))]:
                print('削除するユーザー')
                username=api.get_user(following).name
                print(username)
                print('フォロワー数')
                print(userfollowers)
                api.destroy_friendship(following)