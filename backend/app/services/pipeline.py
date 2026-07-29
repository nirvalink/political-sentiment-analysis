from app.ai.sentiment import analyze_sentiment
from app.ai.emotion import analyze_emotion
from app.ai.keywords import extract_keywords

def analyze_topic(posts):
    sentiment = analyze_sentiment(posts)
    emotion = analyze_emotion(posts)
    keywords = extract_keywords(posts)

    return {
    "sentiment": sentiment,
    "emotion": emotion,
    "keywords": keywords
}