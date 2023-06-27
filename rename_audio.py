import os

def rename_audios(folder_path):
    audio_files = os.listdir(folder_path)
    count = 1

    for file in audio_files:
        if file.endswith(".wav"):
            old_name = os.path.join(folder_path, file)
            new_name = os.path.join(folder_path, f"violence_{count}.wav")

            os.rename(old_name, new_name)
            print(f"Renamed {old_name} to {new_name}")

            count += 1

if __name__ == "__main__":
    folder_path = "C:/Users/Carlita/Desktop/tesis/dataset/Audios/Violence/Audios"
    rename_audios(folder_path)
