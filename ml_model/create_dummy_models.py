# create_dummy_models.py
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import joblib

# Dummy data
X = ["good", "bad", "happy", "sad"]
y = [1, 0, 1, 0]

# Train simple text model
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)
model = MultinomialNB()
model.fit(X_vec, y)

# Save model and vectorizer
joblib.dump(model, "text_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Dummy models created successfully!")
