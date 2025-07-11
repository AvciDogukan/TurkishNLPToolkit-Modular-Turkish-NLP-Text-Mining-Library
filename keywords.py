# turkish_nlp_toolkit/keywords.py

import re
from turkish_nlp_toolkit.tokenization import tokenize
from turkish_nlp_toolkit.utils import TURKISH_STOPWORDS

def extract_keywords(text: str, top_n: int = 10) -> list[str]:
    """
    Metinden durak kelimeleri çıkarıp, kalanları
    frekansa göre sırala ve en çok kullanılan top_n'u döndür.
    """
    freq: dict[str,int] = {}
    for w in tokenize(text.lower()):
        if (w not in TURKISH_STOPWORDS and
            re.match(r"[A-Za-zÇĞİÖŞÜçğıöşü]+$", w)):
            freq[w] = freq.get(w, 0) + 1

    # En yüksek frekanslıları al
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [w for w,_ in sorted_words[:top_n]]
