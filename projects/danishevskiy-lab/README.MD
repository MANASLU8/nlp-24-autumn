# danishevskiy-lab
## Датасет
Используется [Усложненный новостной датасет](http://qwone.com/~jason/20Newsgroups/)(прямая [ссылка](http://qwone.com/~jason/20Newsgroups/20news-bydate.tar.gz) на скачивание) - содержит примеры электронных писем по разным тематикам.

## Проекты
|Проект|Описание|Запуск|Тесты|
|---| --- | --- | ---|
tokenizer | Токенизация на токены. Выделяет некоторые специальные токены - дату, время, номер телефона, имена.| `python tokenizer/__main__.py` | `pytest -v`|
n-grams | Поиск три грамм для токенизированного текста| `python tokenizer/__main__.py`| - |
vectorization| Векторизация токенов с помощью модели W2V| `vectorization/text_prcessing.ipynb` | - |
text_classification | Классификация текста на топик, который текст описывает. Выбирались классы `baseball, hockey, medicine, science`| `text_classification/main.ipynb`| - |
search_and_rag | Реализация поиска в базе данных. База данных основана на используемом датасете с письмами. Добавлен RAG pipline с использованием модели Gemini| `search_and_rag/main.ipynb`| - |