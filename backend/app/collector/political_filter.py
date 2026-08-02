POLITICAL_KEYWORDS = [
    "government",
    "minister",
    "prime minister",
    "pm",
    "chief minister",
    "cm",
    "parliament",
    "assembly",
    "election",
    "vote",
    "voting",
    "bjp",
    "congress",
    "aap",
    "supreme court",
    "high court",
    "policy",
    "bill",
    "ordinance",
    "cabinet",
    "president",
    "governor",
    "modi",
    "rahul gandhi",
    "amit shah",
    "paper leak",
    "cbi",
    "ed",
    "reservation",
    "constitution"
]


def is_political(article_text):
    text = article_text.lower()

    for keyword in POLITICAL_KEYWORDS:
        if keyword in text:
            return True

    return False