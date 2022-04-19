import tweepy
from flair.models import TextClassifier
from flair.data import Sentence

# Set credentials for your account
api_key = "your-api-key"
api_key_secret = "your-api-key-secret"

access_token = "your-access-token"
access_token_secret = "your-access-token-secret"

# Authenticate you
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Retrieve 100 tweets on given user's timeline
tweets = []
for tweet in tweepy.Cursor(api.user_timeline, screen_name='your-target-username', include_rts=False, tweet_mode="extended").items(200):
    tweets.append(tweet.full_text)

# Load model but this is memory-intensive and can take times
sentiment_model = TextClassifier.load("en-sentiment")

# Iterate through the tweets and make the prediction
for tweet in tweets:
    # Convert raw data into processed data
    processed_tweet = Sentence(tweet)
    # Make the prediction
    sentiment_model.predict(processed_tweet)
    with open("results.txt", "a") as f:
        f.write(str(processed_tweet.labels[0]) + "\n")