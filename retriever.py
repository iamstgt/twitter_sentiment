import tweepy


# Set credentials
api_key = "your-api-key"
api_key_secret = "your-api-key-secret"

access_token = "your-access-token"
access_token_secret = "your-access-token-secret"

# Authenticate a user
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Retrieve 200 tweets from target username
tweets = []
for tweet in tweepy.Cursor(api.user_timeline, screen_name='your-target-username', include_rts=False, tweet_mode="extended").items(200):
    tweets.append(tweet.full_text)