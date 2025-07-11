# turkish_nlp_toolkit/sentiment.py

import re

# Örnek pozitif/negatif kelime listeleri; projede dışarıdan genişletilebilir.
POSITIVE_WORDS = {
    "güzel","harika","mükemmel","iyi","sevinç","mutlu","başarılı","hoş","şahane",
    "enfes","keyif","teşekkür","iyi"
}
NEGATIVE_WORDS = {
    "kötü","berbat","rezil","üzgün","korkunç","zor","mutsuz","nefret","hayal kırıklığı",
    "şikayet","istemem","bere","yetersiz"
}

TOKEN_PATTERN = r"[A-Za-zÇĞİÖŞÜçğıöşü']+"

def analyze_sentiment(text: str) -> dict:
    """
    Metindeki pozitif/negatif kelime sayısını sayıp
    - score: [-1.0,1.0] arası normalize edilmiş
    - label: 'positive' | 'negative' | 'neutral'
    - pos_count, neg_count
    döner.
    """
    tokens = re.findall(TOKEN_PATTERN, text.lower())
    pos_count = sum(1 for w in tokens if w in POSITIVE_WORDS)
    neg_count = sum(1 for w in tokens if w in NEGATIVE_WORDS)
    total = pos_count + neg_count
    score = 0.0 if total == 0 else (pos_count - neg_count) / total

    if score > 0:
        label = "positive"
    elif score < 0:
        label = "negative"
    else:
        label = "neutral"

    return {
        "score": score,
        "label": label,
        "positive_count": pos_count,
        "negative_count": neg_count
    }
