from transformers import pipeline

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model=MODEL_NAME
)

def analyze_sentiment(posts):
    return sentiment_pipeline(posts)