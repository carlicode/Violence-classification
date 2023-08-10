import os
from pydub import AudioSegment

def wav_files(carpeta):
    archivos = os.listdir(carpeta)
    archivos_wav = []
    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_archivo) and archivo.endswith(".wav"):
            archivos_wav.append(archivo)
            #print(archivos_wav)
    return archivos_wav

def cortar_archivos(audio_input, chunks_output):
    archivos_wav = wav_files(audio_input)
    for archivo in archivos_wav:
        nombre_original = os.path.splitext(archivo)[0]
        audio = AudioSegment.from_wav(os.path.join(audio_input, archivo))
        duracion_total = len(audio)
        duracion_segmento = 10000  # 15 segundos en milisegundos
        
        if duracion_total <= duracion_segmento:
            # Guardar el audio completo como chunk
            nombre_segmento = f"{nombre_original}.wav"
            audio.export(os.path.join(chunks_output, nombre_segmento), format="wav")
            print(f"Segmento guardado: {nombre_segmento}")
        else:
            segmentos = duracion_total // duracion_segmento

            for i in range(segmentos):
                inicio = i * duracion_segmento
                fin = (i + 1) * duracion_segmento
                segmento = audio[inicio:fin]

                nombre_segmento = f"{nombre_original}_{i+1}.wav"
                segmento.export(os.path.join(chunks_output, nombre_segmento), format="wav")
                print(f"Segmento guardado: {nombre_segmento}")

if __name__ == "__main__":
    audio_input = "C:/Users/Carlita/Desktop/tesis/Experiment 1/people_figthing"
    chunks_output = "C:/Users/Carlita/Desktop/tesis/Experiment 1 chunks/people_figthing"
    cortar_archivos(audio_input, chunks_output)
