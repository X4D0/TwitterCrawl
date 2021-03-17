import tweepy

# CONFIDENTIAL. PLEASE DO NOT USE FOR ANYTHING ELSE!
consumer_key = "rWjIGp083rYmVLoMFHCYZZb6I"
consumer_secret = "EMusm7LmvoUvMSGNHOfF35MW8FF0hgjdvyekryFDLTkwhVH3Pb"
access_token = "82497733-4M0lzZBdYoHTlKSf6AKMWZjfBPWV5FqrDrxp0PsWO"
access_token_secret = "lsHvCEB59D95geSawkOXx7dZkeC8kLAivZZ6ziKwJav3l"

# Authorization Consumer Key and Consumer Secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Set Access to user's Token
auth.set_access_token(access_token, access_token_secret)

# API
api = tweepy.API(auth)

keyword = "#kaesang"
tanggalMulai = "2021-01-16"
jumlahTweet = 15
geo = '-6.200000,106.816666,25km'

tweets = tweepy.Cursor(api.search,
                       q=keyword,
                       lang="id",
                       since=tanggalMulai,
                       geocode=geo).items(jumlahTweet)

with open('SearchTweet.txt', 'a', encoding="utf-8") as f:
    n = 0
    for tweet in tweets:
        n = n + 1
        f.write(str(n) +'. User: ' + tweet.user.screen_name + '\n')
        f.write('   Isi Teks: ' + tweet.text + '\n')
        f.write('\n')
f.close()
