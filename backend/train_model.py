from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

texts = [
    "I love this!", "Great experience", "So bad",  "Awesome", "Worst ever",
    "Totally disappointed", "Such a wonderful experience", "I hate this", "I am so happy", "Amazing!",
    "Worst place ever", "I am very sad", "Superb!", "Not great", "I feel miserable", "Perfect!"
]
labels = [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1]


assert len(texts) == len(labels), f"Texts and labels have different lengths: {len(texts)} != {len(labels)}"

# Improved model with TF-IDF
model = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])

# Train model with more diverse data
model.fit(texts, labels)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "./model/sentiment_model.pkl")
print("✅ Model trained and saved successfully.")
