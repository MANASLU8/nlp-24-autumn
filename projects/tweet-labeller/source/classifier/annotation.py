from tokenizer import tokenize_text
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag

stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


def create_annotation(text):
    sentences = tokenize_text(text)
    annotations = []

    for sentence in sentences:
        sentence_annotations = []
        #получаем части речи для каждого токена
        pos_tags = pos_tag(sentence)

        for token, tag in pos_tags:
            stem = stemmer.stem(token)
            pos = get_wordnet_pos(tag)  # Преобразуем тег POS
            #лемматизируем с частью речи
            lemma = lemmatizer.lemmatize(token, pos)
            sentence_annotations.append((token, stem, lemma))

        annotations.append(sentence_annotations)

    return annotations
