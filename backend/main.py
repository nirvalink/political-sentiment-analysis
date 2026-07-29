from app.data.sample_data import posts
from app.services.pipeline import analyze_topic

report = analyze_topic(posts)

print("=" * 50)
print("PUBLIC PULSE AI")
print("=" * 50)

for i in range(len(posts)):
    print(f"\nPost {i+1}")
    print("Sentiment:", report["sentiment"][i])
    print("Emotion :", report["emotion"][i])

print("\nTop Keywords")
print(report["keywords"])