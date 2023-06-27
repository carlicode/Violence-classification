import os
from pydub import AudioSegment

def calcular_tiempo_total(carpeta):
    tiempo_total = 0

    for root, dirs, files in os.walk(carpeta):
        for file in files:
            ruta_archivo = os.path.join(root, file)
            try:
                audio = AudioSegment.from_file(ruta_archivo)
                duracion = len(audio) / 1000  # Convertir a segundos
                tiempo_total += duracion
            except Exception as e:
                print(f"Error al procesar el archivo {ruta_archivo}: {str(e)}")
                continue

    segundos = int(tiempo_total % 60)
    minutos = int((tiempo_total // 60) % 60)
    horas = int(tiempo_total // 3600)

    return horas, minutos, segundos

if __name__ == "__main__":
    carpeta_audios = "C:/Users/Carlita/Desktop/tesis/dataset/Audios/11 people talking"
    tiempo_horas, tiempo_minutos, tiempo_segundos = calcular_tiempo_total(carpeta_audios)

    print(f"Tiempo total: {tiempo_horas} horas {tiempo_minutos} minutos {tiempo_segundos} segundos")
