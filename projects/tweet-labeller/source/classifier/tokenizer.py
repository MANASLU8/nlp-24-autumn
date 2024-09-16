# source/classifier/tokenizer.py

import re

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'\+?\d{1,4}[\s-]?\(?\d{1,4}\)?[\s-]?\d{1,4}[\s-]?\d{1,4}[\s-]?\d{1,4}'
emoticon_pattern = r'[:;=8][\-o\*]?[)\](\]DPOp]'

combined_pattern = f"({email_pattern}|{phone_pattern}|{emoticon_pattern})"


def tokenize_text(text):
    #(?<!\w\.\w.) - исключаем аббревиатуры до точки (пока только из 2 букв)
    #(? < ![A-Z][a-z]\.) - исключаем Mr./Dr. (пока только мужской пол)
    #(?<=\.|\?|!) - условие сплита, делим если . ? или !
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s', text)

    tokenized_sentences = []

    for sentence in sentences:
        matches = list(re.finditer(combined_pattern, sentence))
        temp_sentence = sentence

        # с помощью маркеров обрабатываем исключительные ситуации (емэйл, номер, эмотикон)
        #TODO проверить с несколькими исключ ситуациями в одном предложении
        for match in matches:
            match_str = match.group(0)
            temp_sentence = temp_sentence.replace(match_str, f"###TOKEN{match.start()}###")

        # \w+ - для слов
        # [^\w\s] - для знаков препинания
        tokens = re.findall(r'###TOKEN\d+###|\w+|[^\w\s]', temp_sentence)

        # меняем временные метки обратно на оригинальные сложные токены
        for match in matches:
            token_idx = tokens.index(f"###TOKEN{match.start()}###")
            tokens[token_idx] = match.group(0)

        tokenized_sentences.append(tokens)

    return tokenized_sentences
