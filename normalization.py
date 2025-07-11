# turkish_nlp_toolkit/normalization.py

import unicodedata
import re

# 1) Unicode normalizasyon (NFKC)
def normalize_unicode(text: str) -> str:
    """
    Metindeki birleşik karakterleri ayırır, uyumlu formata çevirir.
    """
    return unicodedata.normalize("NFKC", text)

# 2) Türkçe’ye özgü case‐folding
def turkish_case_fold(text: str) -> str:
    """
    'İ' → 'i', 'I' → 'ı' dönüşümünü yapıp tümünü küçük harfe çevirir.
    """
    # Önce özel harfleri dönüştür
    text = text.replace("İ", "i").replace("I", "ı")
    # Sonra genel lower
    return text.lower()

# 3) Fazla boşluk/ satır sonu temizliği
def clean_whitespace(text: str) -> str:
    """
    Tüm kontrol karakterleri ve fazla boşlukları tek bir boşluğa indirger,
    baş-sona boşlukları kırpar.
    """
    # Satır sonlarını boşlukla değiştir
    text = re.sub(r"[\r\n]+", " ", text)
    # Birden fazla boşluğu tek boşluğa indir
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# 4) Noktalama birleştirme/normalize
def normalize_punctuation(text: str) -> str:
    """
    Farklı tip tırnak, kısa çizgi vb. öğeleri sadeleştirir.
    """
    # Çift tırnaklar
    text = re.sub(r"[“”«»„‟]", '"', text)
    # Tek tırnaklar
    text = re.sub(r"[‘’‚‛]", "'", text)
    # Çeşitli tire/em/en-dash → normal tire
    text = re.sub(r"[–—―]", "-", text)
    # … (tek karakter üç nokta) → üç nokta
    text = text.replace("…", "...")
    return text

# 5) Hepsini bir arada çağıran normalize fonksiyonu
def normalize(text: str) -> str:
    """
    Sırasıyla:
      1) Unicode NFKC
      2) Türkçe case‐fold
      3) Punctuation normalize
      4) Whitespace clean
    uygular.
    """
    text = normalize_unicode(text)
    text = turkish_case_fold(text)
    text = normalize_punctuation(text)
    text = clean_whitespace(text)
    return text
