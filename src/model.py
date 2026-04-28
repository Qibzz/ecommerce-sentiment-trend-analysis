from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

def build_model():
    """Initialize TF-IDF vectorizer and Naive Bayes model."""
    tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    model = MultinomialNB(alpha=0.1)
    return tfidf, model

def train(tfidf, model, X_train, y_train):
    """Fit TF-IDF and train Naive Bayes."""
    X_tfidf = tfidf.fit_transform(X_train)
    model.fit(X_tfidf, y_train)
    return tfidf, model

def evaluate(model, tfidf, X_test, y_test):
    """Evaluate model and print metrics."""
    X_tfidf = tfidf.transform(X_test)
    y_pred = model.predict(X_tfidf)
    print(f'Accuracy: {accuracy_score(y_test, y_pred):.4f}')
    print(classification_report(y_test, y_pred))
    return y_pred

def predict(model, tfidf, text):
    """Predict sentiment for a single text input."""
    vectorized = tfidf.transform([text])
    result = model.predict(vectorized)[0]
    proba = dict(zip(model.classes_, model.predict_proba(vectorized)[0]))
    return result, proba
