from transformers import pipeline

emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)

def analyze_emotion(posts):
    return emotion_pipeline(posts)