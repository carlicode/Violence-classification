import os
from pydub import AudioSegment

def rename_audio_files(root_folder):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        
        if os.path.isdir(folder_path):
            audio_count = 1

            for filename in os.listdir(folder_path):
                if filename.lower().endswith(('.wav')):
                    file_extension = os.path.splitext(filename)[1]
                    new_filename = f"{folder_name}_{audio_count}{file_extension}"
                    
                    audio_count += 1
                    
                    old_file_path = os.path.join(folder_path, filename)
                    new_file_path = os.path.join(folder_path, new_filename)
                    
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    root_folder = "C:/Users/Carlita/Desktop/tesis/Experiment 2"  

    rename_audio_files(root_folder)
