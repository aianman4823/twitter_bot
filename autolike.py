import tweepy
import config
#xxxxxxxxxxxxxxxxxxxxxは各自取得したAPIをkeyを入れてください。
CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_SECRET = config.ACCESS_SECRET
# インスタンス作成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
# ここで検索をかけています。
# 検索したいワードをqという変数に入れます。今回は"プログラミング"でやってます。
# 取得したいTweet数をcountという変数に入れます。今回は100でやってます。
search_results = api.search(q="プログラミング", count=100)
for result in search_results:
    tweet_id = result.id #Tweetのidを取得
    user_id = result.user._json['id'] #ユーザーのidを取得
    try:
        api.create_favorite(tweet_id) #ファボする
        api.create_friendship(user_id) #フォローする
    except Exception as e:
        print(e)