# 🗳️ AI-Powered Political Sentiment Analysis

An AI-powered Natural Language Processing (NLP) application that analyzes political discussions from social media posts to understand public opinion. The system identifies overall sentiment, detects emotions, and extracts the most important discussion topics using state-of-the-art transformer models.

---

## 📌 Overview

Political discussions on social media generate thousands of opinions every day. Manually understanding public perception is difficult and time-consuming.

This project automates the process by analyzing political text using multiple NLP models and producing structured insights including:

- Sentiment Analysis
- Emotion Detection
- Keyword Extraction

The project is designed with a modular architecture so additional AI capabilities can be integrated easily in future versions.

---

## ✨ Features

- ✅ Political text sentiment analysis
- ✅ Emotion detection using Transformer models
- ✅ Automatic keyword extraction
- ✅ Structured AI report generation
- ✅ Modular AI pipeline
- ✅ Easily extendable architecture

---

## 🧠 AI Models Used

### 1. Sentiment Analysis
**Model:**
`cardiffnlp/twitter-roberta-base-sentiment-latest`

Predicts whether political text is:

- Positive
- Neutral
- Negative

---

### 2. Emotion Detection

**Model:**
`j-hartmann/emotion-english-distilroberta-base`

Detects emotions such as:

- Joy
- Anger
- Fear
- Sadness
- Surprise
- Disgust
- Neutral

---

### 3. Keyword Extraction

A lightweight keyword extraction module identifies the most frequently discussed topics after removing stopwords and unnecessary punctuation.

---

## 🏗️ Project Structure

```
Political-Sentiment-Analysis/
│
├── app/
│   ├── ai/
│   │   ├── sentiment.py
│   │   ├── emotion.py
│   │   ├── keywords.py
│   │   └── pipeline.py
│   │
│   ├── data/
│   └── utils/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

### Programming Language

- Python

### Libraries

- Transformers
- PyTorch
- NLTK
- NumPy

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/political-sentiment-analysis.git
```

Navigate into the project

```bash
cd political-sentiment-analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

## 📊 Sample Output

```
Sentiment:
Positive

Emotion:
Joy

Top Keywords:
election
government
development
economy
jobs
```

---

## 🎯 Future Improvements

- Interactive dashboard
- Data visualization
- Political trend analysis
- Live Twitter/News integration
- Timeline sentiment tracking
- PDF report generation
- Comparative party analysis
- Topic modeling
- Named Entity Recognition (NER)

---

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Natural Language Processing (NLP)
- Transformer Models
- Hugging Face Transformers
- AI Pipeline Design
- Python Project Architecture
- Modular Software Development

---

## 👨‍💻 Author

**Sidhant Jain**

Computer Science Engineering Student

Passionate about Artificial Intelligence, Machine Learning, and Full-Stack Development.

---

## ⭐ If you found this project useful, consider giving it a star!
