import tweepy
import  config
import random
#xxxxxxxxxxxxxxxxxxxxxは各自取得したAPIをkeyを入れてください。
def remove():
    CONSUMER_KEY = config.CONSUMER_KEY
    CONSUMER_SECRET = config.CONSUMER_SECRET
    ACCESS_TOKEN = config.ACCESS_TOKEN
    ACCESS_SECRET = config.ACCESS_SECRET
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