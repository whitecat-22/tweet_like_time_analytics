import tweepy
import matplotlib.pyplot as plt

CONSUMER_KEY="tr1I3ngj2gcM7Zs4whndIpsmO"
CONSUMER_SECRET="QmpY2o53ePr5CgKHtcTObR8m89SSlchmVoI5IlhwRVVkAWpPDa"
ACCESS_TOKEN="1329642301774123008-UOZgbFpHFSRsT005AdVBOsYsZ1OaDP"
ACCESS_SECRET="1cb47maoBgXY6AhLmFiPph1uih28ffte1KwyBuiPA1M62"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# idに取得したいアカウントのユーザーIDをいれる
# search_results = api.user_timeline(id='masason', count=100)
# search_results = api.user_timeline(id='hmikitani', count=100)
# search_results = api.user_timeline(id="tim_cook", count=100)
search_results = api.user_timeline(id='konotarogomame', count=100)

all_likes = []
for search_result in search_results:
    print(search_result._json['created_at'])
    print(search_result._json['text'])
    japan_time = None
    if int(search_result._json['created_at'][11:13]) < 15:
        japan_time = int(search_result._json['created_at'][11:13]) + 9
    elif int(search_result._json['created_at'][11:13]) >= 15:
        japan_time = int(search_result._json['created_at'][11:13]) - 15
    for i in range(int(search_result._json['favorite_count'])):
        all_likes.append(japan_time)


# レーティングの集計を取得してヒストグラムを作成
ratings = all_likes
fig = plt.figure()

axes = fig.add_subplot(xticks=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                               15, 16, 17, 18, 19, 20, 21, 22, 23], yticks=[0, 70000, 150000, 300000, 400000])
axes.hist(ratings, bins=24)

# ヒストグラムを表示
plt.show()
