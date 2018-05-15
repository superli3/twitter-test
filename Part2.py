# Code to find most popular hashtags associated with specified hashtag on twitter

import tweepy
import json
from collections import Counter

# Consumer keys and access tokens, used for OAuth
consumer_key = 'removed'
consumer_secret = 'removed'
access_token = 'removed'
access_token_secret = removed'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Write most recent tweets into Newline Delimited Json file where each line is a JSON dict contain details for a single tweet

json_block = []

for status in tweepy.Cursor(api.user_timeline, screen_name='@realself').items(100):
    tweet_json = json.dumps(status._json)
    json_block.append(tweet_json)

with open('data.txt', 'w') as outfile:
    json.dump(json_block, outfile, indent=2)


#json_block2 = '\n'.join(json_block)
#print json_block2

# Twitter Search API for "#Seattle" and prints to the screen a list of distinct hastags appearing in first 100 results the
# API returns and the number of times each hashtag appears


hashtags_collection = []

for tweet in tweepy.Cursor(api.search, q=('#Seattle')).items(100):
    hashtags = tweet.entities.get('hashtags')
    hashtags2 = [tag['text'].lower() for tag in hashtags]
    hashtags_collection = hashtags_collection + hashtags2

hashtags_counter = Counter(hashtags_collection).most_common()
print hashtags_counter