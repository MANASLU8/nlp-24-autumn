# source/classifier/annotation.py

import os

from tokenizer import tokenize_text
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()

def create_annotation(text):
    sentences = tokenize_text(text)
    annotations = []

    for sentence in sentences:
        sentence_annotations = []
        for token in sentence:
            stem = stemmer.stem(token)
            lemma = lemmatizer.lemmatize(token)
            sentence_annotations.append((token, stem, lemma))
        annotations.append(sentence_annotations)

    return annotations

