TITLE_KEYWORDS = {
    "election": 5,
    "government": 5,
    "minister": 5,
    "prime minister": 5,
    "pm": 5,
    "chief minister": 5,
    "cm": 5,
    "parliament": 5,
    "assembly": 5,
    "policy": 5,
    "bill": 5,
    "cabinet": 5,
    "supreme court": 5,
    "modi": 5,
    "rahul gandhi": 5,
    "amit shah": 5,
    "paper leak": 5
}

TEXT_KEYWORDS = {
    "government": 2,
    "minister": 2,
    "parliament": 2,
    "cabinet": 2,
    "election": 2,
    "vote": 2,
    "policy": 2,
    "court": 2,
    "ed": 2,
    "cbi": 2,
    "paper leak": 2,
    "constitution": 2
}


def calculate_political_score(title, text):
    score = 0

    title = title.lower()
    text = text.lower()

    for keyword, value in TITLE_KEYWORDS.items():
        if keyword in title:
            score += value

    for keyword, value in TEXT_KEYWORDS.items():
        if keyword in text:
            score += value

    return score