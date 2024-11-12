import re
import nltk
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import os

def get_sentences(content):
    sentence_endings_pattern = re.compile(r'(?<!\w\.\w.)(?<!\w\. \w.)(?<![A-Z][a-z]\.)(?<!\s\.\s)(?<=\.|\?|\!)\s(?![A-Z][A-Za-z]\.)(?!\w\. \w.)|(?<![,])\n(?![a-zA-Z0-9])')
    sentences = sentence_endings_pattern.split(content)

    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    sentences_included_key_value = []

    for sentence in sentences:
        key_value_pattern = re.compile(r'[A-Z](\w+-)*\w+(\s\w+)*:[ ]*([\W\w]+[ ,])+(?!,\n)')
        if key_value_pattern.match(sentence):
            add_sentence = re.split(r'(?<!,)\n', sentence)
            sentences_included_key_value.extend(add_sentence)
        else:
            sentences_included_key_value.append(sentence)
    # sentences = [sentence.replace('\n', ' ') for sentence in sentences]
    return sentences_included_key_value
    
def tokenize_sentence(sentence):
    pattern = r'\+?\d[\d\-\(\)\s]{7,}\d' \
              r'|\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' \
              r'|\b(?:Mr|Ms|Mrs|Dr|Prof|St)\.\s[A-Z][a-z]+' \
              r'|\b\d{1,2}:\d{2}\s?(?:[AaPp]\.?[Mm]\.?)\b' \
              r'|\w+|[^\w\s]'
    tokens = re.findall(pattern, sentence)
    tokens = [token.lower() for token in tokens]
    return tokens

def load_nltk():
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')

def stem_tokens(tokens, stemmer):
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

def lemmatize_tokens(tokens, lemmatizer):
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

def process_sentence(sentence, stemmer, lemmatizer):
    tokens = tokenize_sentence(sentence)
    stems = stem_tokens(tokens, stemmer)
    lemmas = lemmatize_tokens(tokens, lemmatizer)
    return tokens, stems, lemmas

def generate_tsv_annotation(sentences):
    tsv_output = []
    
    lemmatizer = WordNetLemmatizer()
    stemmer = SnowballStemmer("english")
    
    for sentence in sentences:
        tokens, stems, lemmas = process_sentence(sentence, stemmer, lemmatizer)
        
        sentence_lines = [
            f"{token}\t{stem}\t{lemma}" for token, stem, lemma in zip(tokens, stems, lemmas)
        ]
        
        tsv_output.append("\n".join(sentence_lines))
        
    return "\n\n".join(tsv_output)

def write_tsv_annotation(project_filepath, sub_directories, filename, tsv_annotation):
    join_symbol = '\\'
    tsv_filepath = '\\assets\\annotated-corpus\\train'
    tsv_directory_path = project_filepath + tsv_filepath + join_symbol + join_symbol.join(sub_directories)
    
    if not os.path.exists(tsv_directory_path):
        os.makedirs(tsv_directory_path)
    with open(tsv_directory_path + join_symbol + filename + '.tsv', 'w') as f:
        f.write(tsv_annotation)

def process_dataset(content, filename, sub_directories, project_filepath):
    print('Process ' + filename)
    sentences = get_sentences(content)
    tsv_annotation = generate_tsv_annotation(sentences)
    
    write_tsv_annotation(project_filepath, sub_directories, filename, tsv_annotation)