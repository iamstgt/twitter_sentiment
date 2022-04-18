from flair.models import TextClassifier
from flair.data import Sentence


# Load model but this is memory-intensive and can take times
sentiment_model = TextClassifier.load("en-sentiment")

with open("tweets.txt", "r") as f:
    tweets = []   
    while True:
        tweet = f.readline()
        if tweet:
            tweets.append(tweet)
        else:
            break

# Iterate through the tweets and make the prediction
for tweet in tweets:
    # Convert raw data into processed data
    processed_tweet = Sentence(tweet)
    # Make the prediction
    sentiment_model.predict(processed_tweet)
    with open("result.txt", "a") as f:
        f.write(str(processed_tweet.labels[0]) + "\n")