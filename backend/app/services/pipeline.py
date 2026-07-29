from app.ai.sentiment import analyze_sentiment
from app.ai.emotion import analyze_emotion

def analyze_topic(posts):
    sentiment = analyze_sentiment(posts)
    emotion = analyze_emotion(posts)

    return {
        "sentiment": sentiment,
        "emotion": emotion
    }