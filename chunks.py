import os
from pydub import AudioSegment

def wav_files(carpeta):
    archivos = os.listdir(carpeta)
    archivos_wav = []
    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_archivo) and archivo.endswith(".WAV"):
            archivos_wav.append(archivo)
            print(archivos_wav)
    return archivos_wav

def cortar_archivos(carpeta):
    archivos_wav = wav_files(carpeta)
    for archivo in archivos_wav:
        print(1)
        nombre_original = os.path.splitext(archivo)[0]
        audio = AudioSegment.from_wav(os.path.join(carpeta, archivo))
        duracion_total = len(audio)
        duracion_segmento = 10000  # 10 segundos en milisegundos
        segmentos = duracion_total // duracion_segmento
        
        for i in range(segmentos):
            inicio = i * duracion_segmento
            fin = (i + 1) * duracion_segmento
            segmento = audio[inicio:fin]

            nombre_segmento = f"{nombre_original}_{i+1}.wav"
            chunks_carpeta = 'C:/Users/Carlita/Desktop/tesis/audios/chunks'
            segmento.export(os.path.join(chunks_carpeta, nombre_segmento), format="wav")
            print(f"Segmento guardado: {nombre_segmento}")

if __name__ == "__main__":
    carpeta = "C:/Users/Carlita/Desktop/tesis/audios"  
    cortar_archivos(carpeta)


