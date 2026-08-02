# Political Sentiment Analysis

An AI-powered Political Sentiment Analysis system that collects live political news, filters articles based on a target topic (currently **Paper Leak**), and performs NLP analysis using state-of-the-art transformer models.

---

## Features

- Live News Collection using RSS
- Automatic Article Extraction
- Topic-based Filtering (Paper Leak)
- Sentiment Analysis
- Emotion Detection
- Keyword Extraction
- Modular AI Pipeline
- Built with Python

---

## Project Structure

```
backend/
│
├── app/
│   ├── ai/
│   │   ├── sentiment.py
│   │   ├── emotion.py
│   │   ├── keywords.py
│   │
│   ├── collector/
│   │   ├── rss_collector.py
│   │   ├── topic_filter.py
│   │   └── political_filter.py
│   │
│   ├── analytics/
│   │   └── political_score.py
│   │
│   └── services/
│       └── pipeline.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# AI Models Used

## 1. Sentiment Analysis

Model

```
cardiffnlp/twitter-roberta-base-sentiment-latest
```

Predicts

- Positive
- Neutral
- Negative

---

## 2. Emotion Detection

Model

```
j-hartmann/emotion-english-distilroberta-base
```

Predicts emotions such as

- Joy
- Anger
- Sadness
- Fear
- Disgust
- Surprise
- Neutral

---

## 3. Keyword Extraction

Uses

```
KeyBERT
```

with

```
all-MiniLM-L6-v2
```

---

# Current Pipeline

```
Indian Express RSS
        │
        ▼
Download Full Article
        │
        ▼
Paper Leak Filter
        │
        ▼
Sentiment Analysis
        │
        ▼
Emotion Detection
        │
        ▼
Keyword Extraction
        │
        ▼
AI Report
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/nirvalink/political-sentiment-analysis.git
```

```bash
cd political-sentiment-analysis/backend
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Required Python Packages

If requirements.txt is unavailable

```bash
pip install transformers
pip install torch
pip install sentence-transformers
pip install keybert
pip install newspaper4k
pip install feedparser
pip install lxml_html_clean
pip install nltk
```

---

# Run the Project

From the backend folder

```bash
python main.py
```

---

# Expected Output

```
PAPER LEAK INTELLIGENCE REPORT

Article

Title:
...

Sentiment:
Negative

Emotion:
Anger

Keywords:
paper leak
UKSSSC
ED
Recruitment
Question Paper
```

---

# Current Topic

The current version analyzes

```
Paper Leak
```

Future versions will support

- Elections
- Government Policies
- Parliament
- Operation Sindoor
- Budget
- Waqf Bill
- User-defined Topics

---

# Future Roadmap

- News Database
- Multi-source News Collection
- AI Summary Generation
- Trend Analysis
- Dashboard
- Charts & Visualizations
- PDF Report Generation
- REST API
- Web Interface
- Deployment

---

# Tech Stack

- Python
- HuggingFace Transformers
- KeyBERT
- Sentence Transformers
- Feedparser
- Newspaper4k
- RSS Feeds

---

# Developed By

**NirvaLink**

AI & Software Solutions
