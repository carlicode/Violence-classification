import os
import speech_recognition as sr

def wav_files(carpeta):
    archivos = os.listdir(carpeta)
    archivos_wav = []
    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_archivo) and archivo.endswith(".wav"):
            archivos_wav.append(archivo)
            
    return archivos_wav

def audio_to_text(audio_folder):
    archivos = wav_files(audio_folder)

    for archivo in archivos:
        # Obtener la ruta completa del archivo de audio
        ruta_audio = os.path.join(audio_folder, archivo)
        
        # Cargar el archivo de audio usando SpeechRecognition
        r = sr.Recognizer()
        with sr.AudioFile(ruta_audio) as source:
            audio = r.record(source)
            
        try:
            # Utilizar el reconocimiento de voz para obtener el texto
            texto = r.recognize_google(audio, language="en")
            print("Texto extraído del audio {}: {}".format(archivo, texto))
            
            # Guardar el texto en un archivo con el mismo nombre del audio en la carpeta de salida
            output_folder = "C:/Users/Carlita/Desktop/tesis/audios/texts/"
            ruta_texto = os.path.join(output_folder + os.path.splitext(archivo)[0] + ".txt")
            with open(ruta_texto, "w") as file:
                file.write(texto)
            print("Texto guardado en:", ruta_texto)
            
        except sr.UnknownValueError:
            print("No se pudo reconocer el audio {}".format(archivo))
        
        except sr.RequestError as e:
            print("Error al procesar el audio {}: {}".format(archivo, str(e)))

if __name__ == '__main__':
    carpeta = "C:/Users/Carlita/Desktop/tesis/audios/chunks/"
    
    audio_to_text(carpeta)
