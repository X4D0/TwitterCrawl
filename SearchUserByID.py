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

# Fetching User by ID
user = api.get_user(82497733)

# Write to txt file
with open('UsersById.txt', 'a') as f:
    f.write('ID : '+user.id_str+'\n')
    f.write('Screen Name : '+user.screen_name+'\n')
    f.write('User Name : '+user.name+'\n')
    f.write('Location : '+user.location+'\n')
    f.write('Followers : '+str(user.followers_count)+'\n')
    f.write('Friends : '+str(user.friends_count)+'\n')
    f.write('Tweets Count : '+str(user.statuses_count)+'\n')
f.close()
open('UsersById.txt', 'rb').read()
