import os

def rename_audios(folder_path, prefix):
    audio_files = [file for file in os.listdir(folder_path) if file.endswith(".wav")]
    count = 1

    for file in audio_files:
        old_name = os.path.join(folder_path, file)
        new_name = os.path.join(folder_path, f"{prefix}_{count+67}.wav")

        os.rename(old_name, new_name)
        print(f"Renamed {new_name}")

        count += 1

if __name__ == "__main__":
    folder_path = "C:/Users/Carlita/Desktop/tesis/Dataset collection/glasses"
    rename_audios(folder_path, "glass_breaking")