import urllib.request
from requests_oauthlib import OAuth1Session # ライブラリ(1)
from bs4 import BeautifulSoup
from TwitterAPI import TwitterAPI
import requests
import tweepy
import os
import datetime
import config

# 各種キーをセット
CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_SECRET = config.ACCESS_SECRET

#apiを取得
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# twitter内を検索し、結果をエクセルに書き込む
for status in api.search(q='プログラミング', lang='ja', result_type='recent',count=100): #qに検索語句,countに検索結果の取得数
    status.user.name #useridが出てくる
    print('user_id'+status.user.name)
    status.user.screen_name#ユーザー名が出てくる
    print('ユーザー名'+status.user.screen_name)
    status.text #ツイート内容が出てくる
    print('ツイート'+status.text)
    created_at=status.created_at
    up=datetime.timedelta(hours=9) #投稿時間が出てくる
    print('投稿時間'+str(created_at+up))