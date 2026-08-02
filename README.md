# 🏛️ Political Sentiment Analysis

An AI-powered Natural Language Processing (NLP) project that analyzes political and public opinion using state-of-the-art transformer models.

Developed by **NirvaLink Pvt. Ltd.**

---

## 📌 Overview

Political Sentiment Analysis is a Python-based application that processes a dataset of public comments and generates meaningful insights using Artificial Intelligence.

The project demonstrates how AI can be used to understand public opinion surrounding political and social issues.

The current demonstration dataset focuses on **NEET Paper Leak** related public comments.

---

# 🚀 Features

- AI-based Sentiment Analysis
- Emotion Detection
- Keyword Extraction
- Executive Summary
- AI-generated Insights
- Sample Comment Analysis
- Lightweight CPU-based implementation

---

# 🤖 AI Models Used

## Sentiment Analysis

Model

```
cardiffnlp/twitter-roberta-base-sentiment-latest
```

Predicts

- Positive
- Neutral
- Negative

---

## Emotion Detection

Model

```
j-hartmann/emotion-english-distilroberta-base
```

Predicts

- Anger
- Joy
- Sadness
- Fear
- Disgust
- Surprise
- Neutral

---

## Keyword Extraction

Library

```
KeyBERT
```

Embedding Model

```
all-MiniLM-L6-v2
```

Extracts the most important discussion topics from the dataset.

---

# 📂 Project Structure

```
political-sentiment-analysis/
│
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   │   ├── sentiment.py
│   │   │   ├── emotion.py
│   │   │   └── keywords.py
│   │   │
│   │   ├── data/
│   │   │   └── sample_data.py
│   │   │
│   │   └── services/
│   │       └── pipeline.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── README.md
└── .gitignore
```

---

# ⚙️ Requirements

- Python 3.10+
- Git

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/nirvalink/political-sentiment-analysis.git
```

Navigate to the backend directory

```bash
cd political-sentiment-analysis/backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

# 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 📊 Current Output

The application generates:

- Dataset Size
- Sentiment Summary
- Emotion Summary
- Top Keywords
- AI-generated Insights
- Sample Comment Analysis

---

# 🛠️ Technologies Used

- Python
- Hugging Face Transformers
- PyTorch
- KeyBERT
- Sentence Transformers
- Scikit-learn

---

# 🔮 Planned Features

- Interactive Dashboard
- Data Visualizations
- Export Reports
- Live News Collection
- Multi-topic Analysis
- Trend Detection
- REST API

---

# 👨‍💻 Developed By

**NirvaLink Pvt. Ltd.**

AI & Software Solutions

---

# 📄 License

This project is intended for educational, research and demonstration purposes.