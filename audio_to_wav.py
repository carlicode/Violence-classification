from pydub import AudioSegment
import os

def convert_to_wav(input_path, output_folder):
    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_path):
        if filename.lower().endswith(('.mp3', '.ogg', '.flac', '.wav', '.aac')):
            input_file_path = os.path.join(input_path, filename)
            output_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".wav")

            audio = AudioSegment.from_file(input_file_path)

            # Si el archivo no está en formato WAV, convertirlo
            if audio.frame_count() > 0 and audio.frame_rate > 0:
                audio.export(output_file_path, format="wav")
                print("Archivo convertido a formato WAV:", output_file_path)
            else:
                print("El archivo ya está en formato WAV o no se pudo cargar:", input_file_path)

if __name__ == "__main__":
    input_folder = "C:/Users/Carlita/Desktop/tesis/Dataset collection/freesound crying"
    output_folder = "C:/Users/Carlita/Desktop/tesis/Experiment 2/freesound crying" 

    convert_to_wav(input_folder, output_folder)
