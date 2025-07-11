# turkish_nlp_toolkit/stemming.py

try:
    # PyPI’den gelen TurkishStemmer sınıfı
    from TurkishStemmer import TurkishStemmer as _TS
    _stemmer = _TS()
except ImportError:
    raise ImportError(
        "TurkishStemmer paketi bulunamadı. "
        "Lütfen `pip install TurkishStemmer` ile yükleyin."
    )

def stem_word(word: str) -> str:
    """
    Tek bir kelimeyi stem’ine (köküne) indirger.
    Örnek: stem_word("doktoruymuşsunuz")  → "doktor"
    """
    return _stemmer.stem(word)

def stem_tokens(tokens: list[str]) -> list[str]:
    """
    Bir token listesi alır, her birini küçük harfe çevirmeden doğrudan stem’ler.
    """
    return [stem_word(tok) for tok in tokens]
