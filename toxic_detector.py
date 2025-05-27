# toxic_detector.py
from transformers import pipeline

classifier = pipeline("text-classification", model="unitary/toxic-bert", truncation=True)

def is_toxic(text):
    result = classifier(text)[0]
    label = result['label'].lower()
    score = result['score']
    return label, score
