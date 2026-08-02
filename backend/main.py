from app.collector.rss_collector import fetch_news
from app.services.pipeline import analyze_article

articles = fetch_news()

print("=" * 60)
print("PAPER LEAK INTELLIGENCE REPORT")
print("=" * 60)

for index, article in enumerate(articles, start=1):

    result = analyze_article(article["text"])

    print(f"\nArticle {index}")
    print("-" * 60)

    print(f"Title      : {article['title']}")
    print(f"Published  : {article['published']}")
    print(f"Source     : {article['link']}")

    print("\nAI ANALYSIS")
    print(f"Sentiment  : {result['sentiment']}")
    print(f"Emotion    : {result['emotion']}")
    print(f"Keywords   : {result['keywords']}")

    print("\n" + "=" * 60)