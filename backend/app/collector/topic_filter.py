PAPER_LEAK_KEYWORDS = [
    "paper leak",
    "exam leak",
    "question paper",
    "uksssc",
    "neet",
    "ugc net",
    "recruitment exam",
    "exam scam"
]


def is_paper_leak_article(title, text):
    content = (title + " " + text).lower()

    for keyword in PAPER_LEAK_KEYWORDS:
        if keyword in content:
            return True

    return False