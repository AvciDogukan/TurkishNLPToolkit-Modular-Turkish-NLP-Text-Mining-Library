# turkish_nlp_toolkit/summarization.py

import re
from turkish_nlp_toolkit.tokenization import tokenize
from turkish_nlp_toolkit.utils import TURKISH_STOPWORDS

def summarize(text: str, n_sentences: int = 3) -> str:
    """
    Metni cümlelere böl, her cümlenin kelime skorunu frekansa göre hesapla,
    en yüksek puanlı n_sentences cümleyi sırayla birleştir.
    """
    # 1) Cümlelere böl
    sentences = re.split(r'(?<=[\.!?])\s+', text.strip())
    if not sentences or text.strip() == "":
        return ""

    # 2) Metindeki kelime frekansları
    freq: dict[str,int] = {}
    for w in tokenize(text.lower()):
        if w not in TURKISH_STOPWORDS and re.match(r"[A-Za-zÇĞİÖŞÜçğıöşü]+$", w):
            freq[w] = freq.get(w, 0) + 1

    # 3) Her cümlenin skoru
    scores: dict[str,float] = {}
    for sent in sentences:
        score = sum(freq.get(w, 0) for w in tokenize(sent.lower()))
        scores[sent] = score

    # 4) En yüksek skorlu cümleleri al
    selected = sorted(scores, key=lambda s: scores[s], reverse=True)[:n_sentences]
    # Orijinal sırayla döndürmek için:
    ordered = [s for s in sentences if s in selected]
    return " ".join(ordered)
