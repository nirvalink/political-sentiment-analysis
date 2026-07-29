from app.ai.sentiment import analyze_sentiment

def analyze_topic(posts):
    sentiment = analyze_sentiment(posts)

    return {
        "sentiment": sentiment
    }