from datasets import load_dataset
from .file_utils import process_and_save_annotations, create_directories
import os

def main():

    base_dir = f"../../assets/annotated-corpus"

    train_dir = os.path.join(base_dir, "train")
    test_dir = os.path.join(base_dir, "test")

    ds = load_dataset("cardiffnlp/tweet_eval", "sentiment")

    label_map = {
        0: 'negative',
        1: 'neutral',
        2: 'positive'
    }

    # Создание директорий для классов в train и test
    train_labels = [label_map[label] for label in ds['train']['label']]
    test_labels = [label_map[label] for label in ds['test']['label']]

    create_directories(train_dir, train_labels)
    create_directories(test_dir, test_labels)

    process_and_save_annotations(ds, 'train', label_map, train_dir)
    process_and_save_annotations(ds, 'test', label_map, test_dir)

if __name__ == "__main__":
    main()
