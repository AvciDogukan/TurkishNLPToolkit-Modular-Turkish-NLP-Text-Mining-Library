
# Turkish NLP Toolkit

A modular and extensible Natural Language Processing (NLP) toolkit for Turkish text.  
Provides core text mining functions such as preprocessing, tokenization, stemming, normalization, syllabification, sentiment analysis, summarization, and keyword extraction.  
Ideal for research, educational projects, and rapid NLP prototyping in Turkish.

---

## 🚀 Features

- **Text Preprocessing:** Unicode normalization, Turkish case folding, stopword removal, stemming support.
- **Tokenization & Detokenization:** Word, number, and punctuation-aware tokenization with apostrophe splitting.
- **Stemming:** Turkish root extraction using [TurkishStemmer](https://pypi.org/project/TurkishStemmer/).
- **Sentiment Analysis:** Basic positive/negative polarity scoring for Turkish sentences.
- **Summarization:** Frequency-based extractive sentence summarization.
- **Syllabification:** Turkish-specific syllable segmentation for words and sentences.
- **Keyword Extraction:** Frequency-based top-N keyword extraction, stopwords excluded.
- **Normalization:** Unicode, case, punctuation and whitespace normalization routines.

---

## 📂 File & Module Structure

turkish-nlp-toolkit/
│
├── preprocessing.py
├── tokenization.py
├── normalization.py
├── stemming.py
├── sentiment.py
├── summarization.py
├── keywords.py
├── syllabification.py
└── README.md

- preprocessing.py — Complete text cleaning and normalization pipeline.
- tokenization.py — Word, number, and punctuation-level tokenization; detokenizer included.
- normalization.py — Unicode, Turkish-case, whitespace and punctuation normalization.
- stemming.py — Turkish word stemming using external library.
- sentiment.py — Simple Turkish sentiment analysis via word lists.
- summarization.py — Frequency-based extractive text summarization.
- keywords.py — Top-N keyword extraction from input text.
- syllabification.py — Turkish word and sentence syllabification utilities.

---

## 🛠️ Example Usage

from turkish_nlp_toolkit.preprocessing import preprocess
from turkish_nlp_toolkit.sentiment import analyze_sentiment
from turkish_nlp_toolkit.summarization import summarize
from turkish_nlp_toolkit.keywords import extract_keywords
from turkish_nlp_toolkit.syllabification import syllabify_text

# Preprocessing
tokens = preprocess("Bu harika bir açık kaynak NLP projesi!", remove_stopwords=True, do_stemming=True)

# Sentiment
result = analyze_sentiment("Bu proje gerçekten mükemmel ve faydalı.")

# Summarization
summary = summarize("Çok uzun bir Türkçe metin...")

# Keywords
kw = extract_keywords("Projede birden çok NLP özelliği var.", top_n=5)

# Syllabification
syllables = syllabify_text("Merhaba dünya")

---

## ⚡️ Requirements

- Python 3.8+
- TurkishStemmer (for stemming support):

pip install TurkishStemmer

---

## 📝 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author & Contact

Developed by Doğukan Avcı

- Email: hulavci121@gmail.com
- LinkedIn: https://www.linkedin.com/in/doğukanavcı-119541229/
- GitHub: https://github.com/AvciDogukan

For questions, suggestions, or collaboration, feel free to get in touch!

---
