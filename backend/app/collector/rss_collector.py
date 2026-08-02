import feedparser
from newspaper import Article
from app.collector.political_filter import is_political
from app.analytics.political_score import calculate_political_score
from app.collector.topic_filter import is_paper_leak_article

RSS_URL = "https://indianexpress.com/section/india/feed/"


def fetch_news():
    feed = feedparser.parse(RSS_URL)

    articles = []

    for entry in feed.entries[:10]:
        try:
           article = Article(entry.link)
           article.download()
           article.parse()

           if not is_paper_leak_article(entry.title, article.text):
             continue

        #    print(f"{entry.title} -> {len(article.text)} characters")

           score = calculate_political_score(
                article.title,
                article.text
           )
        #    if score < 8:
        #         continue

        #    if not is_political(article.text):
        #       continue

           articles.append({
             "title": entry.title,
             "link": entry.link,
             "published": entry.published,
             "text": article.text,
             "score": score
            })

        except Exception as e:
             print(f"Failed to fetch article: {entry.link}")

    return articles