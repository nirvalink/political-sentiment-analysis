from collections import Counter
import re


def extract_keywords(posts, top_n=10):
    words = []

    for post in posts:
        cleaned = re.sub(r"[^a-zA-Z\s]", "", post.lower())
        words.extend(cleaned.split())

    stop_words = {
        "the", "is", "a", "an", "and", "or", "to", "of",
        "in", "on", "for", "with", "this", "that", "it",
        "be", "are", "was", "were", "i", "we", "they",
        "you", "our", "your", "their"
    }

    filtered = [word for word in words if word not in stop_words and len(word) > 2]

    return Counter(filtered).most_common(top_n)