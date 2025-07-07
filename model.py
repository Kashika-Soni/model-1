from transformers import pipeline

# Load Hugging Face model
classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    if not text.strip():
        return "Please enter some text."
    result = classifier(text)
    label = result[0]['label']
    score = round(result[0]['score'] * 100, 2)
    return f"Sentiment: {label} ({score}%)"
