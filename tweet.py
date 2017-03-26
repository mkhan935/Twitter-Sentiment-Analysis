import tweepy
import sys
from textblob import TextBlob


''' The goal of this script, is to search the twitter api for tweets on the word of our choosing,
I chose healthcare as at the time writing this script it is a topic of great concern,
the script then uses TextBlob to analyize the sentiment of the user,
polarity measures how positive or negative some text is, subjectivity measures
how much of opinion or factual a text is, this is all outputted into a test.txt file.
I did this just to learn how to use API and it seemed like a fun topic floating around stackoverflow.

the consumer_key,consumer_secret, access_token, access_token_secret are your own personal api generated keys,
i have left them blank as I do not wish to share my keys, please sign up for the twiiter api and use your own, it was crazy fun trying
this on controversial topics, machine learning is the future :) and analyzing data has been the present norm  '''


consumer_key = 'your Key goes here'
consumer_secret = 'your Key goes here'

access_token = 'your Key goes here'
access_token_secret = 'your Key goes here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('healthcare')
f=open("test.txt",'w')
sys.stdout = f

for tweet in public_tweets:
    print(tweet.text.encode("utf-8"))
    analysis = TextBlob(tweet.text)
    print('\n',analysis.sentiment)
f.close()
