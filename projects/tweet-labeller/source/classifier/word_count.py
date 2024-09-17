from datasets import load_dataset
from .tokenizer import tokenize_text


def count_words(dataset_split):
    word_count = 0
    for example in dataset_split:
        text = example['text']
        tokenized_text = tokenize_text(text)
        # считаем количество токенов (слов)
        word_count += sum(len(sentence) for sentence in tokenized_text)
    return word_count


def main():
    ds = load_dataset("cardiffnlp/tweet_eval", "sentiment")

    train_word_count = count_words(ds['train'])
    test_word_count = count_words(ds['test'])

    print(f"Количество слов в тренировочном наборе: {train_word_count}")
    print(f"Количество слов в тестовом наборе: {test_word_count}")


if __name__ == "__main__":
    main()
