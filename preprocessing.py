# turkish_nlp_toolkit/preprocessing.py

from .normalization import normalize
from .tokenization import tokenize
from .utils import TURKISH_STOPWORDS
from .stemming import stem_tokens

def preprocess(
    text: str,
    remove_stopwords: bool = False,
    do_stemming: bool = False
) -> list[str]:
    """
    Metin ön işleme pipeline'ı:
      1) normalize(text)
      2) tokenize(...)
      3) gerekirse stop-word çıkar
      4) gerekirse stem uygula

    Args:
      text: girdi metni
      remove_stopwords: durak kelimeleri listeden çıkar
      do_stemming: tokenları stem_word ile köklerine indirger

    Returns:
      İşlenmiş token listesi
    """
    # 1) Normalize
    txt = normalize(text)

    # 2) Tokenize
    toks = tokenize(txt)

    # 3) Stop-word çıkarma
    if remove_stopwords:
        toks = [t for t in toks if t.lower() not in TURKISH_STOPWORDS]

    # 4) Stemming
    if do_stemming:
        toks = stem_tokens(toks)

    return toks
