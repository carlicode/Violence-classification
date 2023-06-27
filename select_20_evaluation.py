import os
import random
import shutil

def randomly_select_files(source_folder, destination_folder):
    files = os.listdir(source_folder)
    total_files = len(files)
    selected_files_count = int(total_files * 0.2)  # Selecting 20% of the files

    selected_files = random.sample(files, selected_files_count)

    for file in selected_files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
        print(f"File {file} moved to {destination_folder}")

if __name__ == "__main__":
    source_folder = "C:/Users/Carlita/Desktop/tesis/experiment 1/Train/No Violence"
    destination_folder = "C:/Users/Carlita/Desktop/tesis/experiment 1/Test/No Violence"
    randomly_select_files(source_folder, destination_folder)
