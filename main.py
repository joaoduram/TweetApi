import tweepy
import pandas as pd

consumer_key= ''
consumer_secret= ''
access_token= ''
access_token_secret= ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
client = tweepy.Client(consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_token_secret)
query = 'query'
tweets = client.search_recent_tweets(query=query, max_results=100, user_auth=True)
output = []

for tweet in tweets.data:
    output.append(tweet.text)
df = pd.DataFrame(tweets)
df.to_csv('output.csv')