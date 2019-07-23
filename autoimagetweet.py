import twitter
import config
auth = twitter.OAuth(
CONSUMER_KEY = config.CONSUMER_KEY,
CONSUMER_SECRET = config.CONSUMER_SECRET,
ACCESS_TOKEN = config.ACCESS_TOKEN,
ACCESS_SECRET = config.ACCESS_SECRET)

t = twitter.Twitter(auth=auth)

#ツイートのみ
status="Hello,World." #投稿するツイート
t.statuses.update(status=status) #Twitterに投稿

# #画像付きツイート
# pic=""#画像を投稿するなら画像のパス
# with open(pic,"rb") as image_file:
#   image_data=image_file.read()
#   pic_upload = twitter.Twitter(domain='upload.twitter.com',auth=auth)
#   id_img1 = pic_upload.media.upload(media=image_data)["media_id_string"]
# t.statuses.update(status=status,media_ids=",".join([id=img1]))
