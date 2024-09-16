# source/classifier/file_utils.py

import os

from annotation import create_annotation


# Функция для создания директории для классов
def create_directories(base_dir, labels):
    for label in labels:
        dir_path = os.path.join(base_dir, label)
        os.makedirs(dir_path, exist_ok=True)


# Функция для сохранения аннотаций

# source/classifier/file_utils.py

def save_annotation(directory, label, doc_id, annotation):
    file_path = os.path.join(directory, label, f"{doc_id}.tsv")

    with open(file_path, 'w', encoding='utf-8') as f:
        for sentence in annotation:
            for token, stem, lemma in sentence:
                f.write(f"{token}\t{stem}\t{lemma}\n")
            f.write("\n")


# def process_and_save_annotations(dataset, split, label_map, output_dir):
#     for i, example in enumerate(dataset[split]):
#         text = example['text']
#         label = label_map[example['label']]  # Преобразование метки в текстовый класс
#         doc_id = f"{i:03d}"  # Используем номер записи как идентификатор
#         annotation = create_annotation(text)
#         if text == 'Don\'t hit the Twitter for bookings and features.. Contact ransom201beats@gmail.com GANGSTA GRILLZ SEPT 20TH WINTERS HERE!!!':
#             print(i, annotation)
#
#         save_annotation(output_dir, label, doc_id, annotation)
#
#     print(f"Обработка и сохранение аннотаций для {split} завершена. Аннотации сохранены в {output_dir}.")

def process_and_save_annotations(dataset, split, label_map, output_dir):
    for i, example in enumerate(dataset[split]):
        text = example['text']
        label = label_map[example['label']]  # Преобразование метки в текстовый класс
        doc_id = f"{i:03d}"  # Используем номер записи как идентификатор
        if text == 'Don\'t hit the Twitter for bookings and features.. Contact ransom201beats@gmail.com GANGSTA GRILLZ SEPT 20TH WINTERS HERE!!!':
            annotation = create_annotation(text)
            print(i, annotation)
            save_annotation(output_dir, label, doc_id, annotation)

    print(f"Обработка и сохранение аннотаций для {split} завершена. Аннотации сохранены в {output_dir}.")
