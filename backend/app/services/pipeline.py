from app.ai.sentiment import analyze_sentiment
from app.ai.emotion import analyze_emotion
from app.ai.keywords import extract_keywords


def analyze_article(article_text):
    sentiment = analyze_sentiment([article_text])[0]
    emotion = analyze_emotion([article_text])[0]
    keywords = extract_keywords([article_text])

    return {
        "sentiment": sentiment,
        "emotion": emotion,
        "keywords": keywords
    }