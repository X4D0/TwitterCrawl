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

# Fetching User Network
akun = "dafuq_haris"
userfollowers = api.followers(akun)
userfollowing = api.friends(akun)
with open('UserNetworks.txt', 'a') as f:
    f.write(akun+' Networks\n')
    f.write('Followers : \n')
    for follower in userfollowers:
        f.write(follower.screen_name+'\n')
    f.write('\nFollowing : \n')
    for friends in userfollowing:
        f.write(friends.screen_name+'\n')
    f.write('\n')
f.close()
