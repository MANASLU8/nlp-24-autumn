# main.py

from datasets import load_dataset
from file_utils import process_and_save_annotations

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

    process_and_save_annotations(ds, 'train', label_map, train_dir)
    process_and_save_annotations(ds, 'test', label_map, test_dir)

if __name__ == "__main__":
    main()
