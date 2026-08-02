from collections import Counter

from app.data.sample_data_100 import posts
from app.services.pipeline import analyze_topic

def generate_ai_insights(sentiment_count, emotion_count, keywords):
    total = sum(sentiment_count.values())

    negative_pct = (sentiment_count.get("Negative", 0) / total) * 100
    neutral_pct = (sentiment_count.get("Neutral", 0) / total) * 100
    positive_pct = (sentiment_count.get("Positive", 0) / total) * 100

    dominant_emotion = emotion_count.most_common(1)[0][0]

    top_keywords = ", ".join(
        [keyword for keyword, _ in keywords[:5]]
    )

    print("\n" + "=" * 60)
    print("AI INSIGHTS")
    print("=" * 60)

    print(f"• {negative_pct:.1f}% of the analysed comments express negative sentiment.")
    print(f"• {neutral_pct:.1f}% of the comments are neutral.")
    print(f"• {positive_pct:.1f}% of the comments are positive.")

    print(f"\n• Dominant public emotion: {dominant_emotion}")

    print(f"\n• Most discussed topics:")
    print(f"  {top_keywords}")

    if negative_pct > 50:
        print("\n• Public confidence appears to be low regarding the fairness of the examination process.")

    if positive_pct > 20:
        print("• A noticeable section of the public supports recent reforms and stricter action against paper leaks.")

    print("• Continued investigation and transparent reforms are likely to improve public trust.")

# Analyze all sample posts
report = analyze_topic(posts)

# -----------------------------
# Sentiment Summary
# -----------------------------
sentiment_labels = [
    item["label"].capitalize()
    for item in report["sentiment"]
]

sentiment_count = Counter(sentiment_labels)

# -----------------------------
# Emotion Summary
# -----------------------------
emotion_labels = [
    item["label"].capitalize()
    for item in report["emotion"]
]

emotion_count = Counter(emotion_labels)

print("=" * 60)
print("PUBLIC PULSE AI")
print("=" * 60)

print(f"\nDataset Size : {len(posts)} Public Comments")

print("\nSENTIMENT SUMMARY")
print("-" * 60)
print(f"Positive : {sentiment_count.get('Positive', 0)}")
print(f"Neutral  : {sentiment_count.get('Neutral', 0)}")
print(f"Negative : {sentiment_count.get('Negative', 0)}")

print("\nEMOTION SUMMARY")
print("-" * 60)

for emotion, count in emotion_count.most_common():
    print(f"{emotion:<12}: {count}")


print("\nTOP KEYWORDS")
print("=" * 60)

for keyword, frequency in report["keywords"]:
    print(f"{keyword:<20} {frequency}")

generate_ai_insights(
    sentiment_count,
    emotion_count,
    report["keywords"]
)

print("\n" + "=" * 60)
print("SAMPLE ANALYSIS")
print("=" * 60)

# Show only first 5 comments
for i, post in enumerate(posts[:5]):
    sentiment = report["sentiment"][i]
    emotion = report["emotion"][i]

    print("\n" + "-" * 60)
    print(f"Comment {i + 1}")

    print("\nText:")
    print(post)

    print("\nSentiment:")
    print(f"{sentiment['label'].capitalize()} ({sentiment['score']*100:.2f}%)")

    print("\nEmotion:")
    print(f"{emotion['label'].capitalize()} ({emotion['score']*100:.2f}%)")