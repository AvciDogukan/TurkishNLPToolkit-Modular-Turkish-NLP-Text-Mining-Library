# turkish_nlp_toolkit/tokenization.py

import re

# Eğer "regex" kütüphanesi yüklüyse Unicode desteğiyle kullan
try:
    import regex as re_unicode
    _findall = re_unicode.findall
    # \p{L} Unicode harfleri, rakamları ve noktalama işaretlerini yakalar
    _WORD_PUNCT_PATTERN = r"\p{L}[\p{L}']*|\d+|[^\s\p{L}\d]"
except ImportError:
    _findall = re.findall
    _WORD_PUNCT_PATTERN = r"[A-Za-zÇĞİÖŞÜçğıöşü']+|\d+|[^\sA-Za-zÇĞİÖŞÜçğıöşü\d]"

VOWELS = set("aeıioöuüAEIİOÖUÜ")

def tokenize(text: str) -> list[str]:
    """
    Metni kelime, sayı ve noktalama işaretleri bazlı token’lara ayırır.
    Apostrof (kesme işareti) ile ayrılmış ekleri de ayırır:
      "Ankara'da" → ["Ankara", "da"]
    """
    raw_tokens = _findall(_WORD_PUNCT_PATTERN, text)
    tokens: list[str] = []
    for tok in raw_tokens:
        # Apostroflu ekleri parçala
        if "'" in tok:
            parts = tok.split("'")
            tokens.extend([p for p in parts if p])
        else:
            tokens.append(tok)
    return tokens

def detokenize(tokens: list[str]) -> str:
    """
    Token listesini tekrar metne çevirir:
      - Token'ları boşlukla birleştirir,
      - Noktalama işaretlerinden önceki fazladan boşluğu siler.
    Örnek:
      ["Merhaba","dünya","!"] → "Merhaba dünya!"
    """
    text = " ".join(tokens)
    # Noktalama işaretlerinden önceki boşluğu kaldır
    text = re.sub(r"\s+([.,!?;:%])", r"\1", text)
    return text
