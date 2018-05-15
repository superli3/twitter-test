# code to output top 100 tweets from a twitter account and output to delimited json file

import tweepy
import json
from bson import json_util

# Consumer keys and access tokens, used for OAuth
consumer_key = 'removed'
consumer_secret = 'removed'
access_token = 'removed'
access_token_secret = 'removed'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

json_block = []

for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump').items(100):
    tweet_json = json.dumps(status._json)
    json_block.append(tweet_json)


with open('data.txt', 'w') as outfile:
    json.dump(json_block, outfile, indent=2)


json_block2 = '\n'.join(json_block)
print json_block2