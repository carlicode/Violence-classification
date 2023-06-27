import os
from moviepy.editor import *

def convert_videos_to_audio(video_folder, audio_folder):
    video_files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.mkv', '.avi'))]

    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)

    for video_file in video_files:
        video_path = os.path.join(video_folder, video_file)
        audio_name = os.path.splitext(video_file)[0] + '.wav'
        audio_path = os.path.join(audio_folder, audio_name)

        video = VideoFileClip(video_path)
        audio = video.audio

        audio.write_audiofile(audio_path, codec='pcm_s16le')

        video.close()
        audio.close()

# Ejemplo de uso
video_folder = 'C:/Users/Carlita/Desktop/tesis/dataset/Real Life Violence Dataset Violence'
audio_folder = 'C:/Users/Carlita/Desktop/tesis/dataset/Audio'
convert_videos_to_audio(video_folder, audio_folder)
