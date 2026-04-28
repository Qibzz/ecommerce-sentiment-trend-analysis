import re

STOPWORDS_ID = set([
    'yang', 'dan', 'di', 'ke', 'dari', 'ini', 'itu', 'dengan', 'untuk',
    'tidak', 'ada', 'saya', 'aku', 'kamu', 'kami', 'kita', 'mereka',
    'sudah', 'bisa', 'juga', 'tapi', 'atau', 'karena', 'jadi', 'kalau',
    'aja', 'ya', 'yg', 'ga', 'gak', 'nggak', 'nya', 'lagi', 'buat',
    'nih', 'sih', 'deh', 'dong', 'banget', 'udah', 'sama', 'kayak',
    'terus', 'masih', 'mau', 'lg', 'sy', 'dr', 'dlm', 'sdh', 'dgn',
    'tp', 'krn', 'lebih', 'pun', 'kak', 'kalo', 'shopee', 'aplikasi',
    'app', 'apk', 'hi', 'hai', 'maaf', 'terima', 'kasih', 'terimakasih'
])

def clean_text(text):
    """Clean and tokenize Indonesian text."""
    if not isinstance(text, str):
        return ''
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = [w for w in text.split() if w not in STOPWORDS_ID and len(w) > 2]
    return ' '.join(tokens)

def categorize_sentiment(score):
    """Map numeric score to sentiment label."""
    if score <= 2:
        return 'Negatif'
    elif score == 3:
        return 'Netral'
    else:
        return 'Positif'
