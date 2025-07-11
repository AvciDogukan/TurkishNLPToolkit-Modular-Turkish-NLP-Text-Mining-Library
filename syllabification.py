# turkish_nlp_toolkit/syllabification.py

import re

# Türkçe ünlüler
VOWELS = set("aeıioöuüAEIİOÖUÜ")

def syllabify_word(word: str) -> list[str]:
    """
    Tek bir kelimeyi hecelere böler.
    Kurallar (basitleştirilmiş):
      1. Her ünlü yeni bir hece başlatır.
      2. Ünlüler arasındaki tekli ünsüz, takip ettiği heceye katılır.
      3. Ünlüler arasındaki çoklu ünsüz takımının son ünsüzü yeni heceye katılır.
    Örnek: "kitaptan" → ["ki", "tap", "tan"]
    """
    # Ünlü indekslerini bul
    vowel_idxs = [i for i, ch in enumerate(word) if ch in VOWELS]
    if not vowel_idxs:
        return [word]  # ünsüzler veya rakam gibi heceye bölünmez

    syllables = []
    start = 0

    for i in range(len(vowel_idxs) - 1):
        v_idx = vowel_idxs[i]
        next_v = vowel_idxs[i + 1]
        # consonant cluster between these vowels
        cluster = word[v_idx + 1 : next_v]
        if len(cluster) <= 1:
            # tekli ünsüz ya da direkt komşu → heceyi ünlüden sonraki her şeye kadar kes
            cut = v_idx + 1
        else:
            # birden çok ünsüz: son ünsüzü sonraki heceye bırak
            cut = v_idx + 1 + len(cluster) - 1
        syllables.append(word[start : cut])
        start = cut

    # son hece
    syllables.append(word[start:])

    return syllables


def syllabify_text(text: str) -> list[list[str]]:
    """
    Bir metindeki her kelimeyi hecelere böler.
    Noktalama ve boşluklarla ayrılmış parçaları ayrı kelime sayar.
    """
    # Basitçe boşluk ve noktalama ile kelimelere ayır
    words = re.findall(r"[A-Za-zÇĞİÖŞÜçğıöşü']+", text)
    return [syllabify_word(w) for w in words]


if __name__ == "__main__":
    # Hızlı deneme
    examples = ["kitap", "kitaptan", "merhaba", "örnekleme", "ağaç"]
    for word in examples:
        print(f"{word} → {syllabify_word(word)}")
