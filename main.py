from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from flair.models import TextClassifier
from flair.data import Sentence

app = FastAPI()


class TweetModel(BaseModel):
    tweet: str

@app.post("/{tweet}")
def sentiment(tweet):
    # Load model but this is memory-intensive and can take time
    sentiment_model = TextClassifier.load("en-sentiment")
    # Convert raw data into processed data
    processed_tweet = Sentence(tweet)
    # Make the prediction
    sentiment_model.predict(processed_tweet)
    return str(processed_tweet)