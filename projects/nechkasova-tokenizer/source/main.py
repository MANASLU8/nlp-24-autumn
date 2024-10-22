import sys
import os
from tokenizer import process_dataset, load_nltk

def read_content(file_path):
    filename = file_path.split('\\')[-1]
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content, filename
    except Exception as e:
        print(f"Couldn't read file {filename}: {e}")
        return None
                

def read_files_in_directory(directory, sub_directories):
    join_symbol = '\\'
    project_filepath = join_symbol.join(sys.argv[0].split(join_symbol)[:-2])
    if os.path.isfile(directory):
        content, filename = read_content(directory)
        process_dataset(content, filename, sub_directories, project_filepath)
    else:
        current_sub_directories = sub_directories[:]
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            if os.path.isfile(file_path):
                content, filename = read_content(file_path)
                process_dataset(content, filename, current_sub_directories, project_filepath)
            else:
                new_sub_directory = file_path.split('\\')[-1]
                updated_sub_directories = current_sub_directories + [new_sub_directory]
                
                read_files_in_directory(file_path, updated_sub_directories)



if len(sys.argv) > 1:
    dataset_path_file = sys.argv[1]
    print(f"Path to choosen dataset: {dataset_path_file}")
else:
    print("Coundn't find argument")

load_nltk()
sub_directories = []
read_files_in_directory(dataset_path_file, sub_directories)