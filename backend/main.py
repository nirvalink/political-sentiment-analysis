from app.data.sample_data import posts
from app.services.pipeline import analyze_topic

report = analyze_topic(posts)

print("=" * 50)
print("PUBLIC PULSE AI")
print("=" * 50)

for item in report["sentiment"]:
    print(item)