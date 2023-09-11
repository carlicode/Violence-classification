import os
import random
import shutil

def seleccionar_y_guardar_archivos(carpetapath, destino, cantidad=120 ):
    archivos_wav = [archivo for archivo in os.listdir(carpetapath) if archivo.endswith(".wav")]

    if len(archivos_wav) < cantidad:
        print(f"No hay suficientes archivos .wav en la carpeta {carpetapath}.")
        return

    archivos_seleccionados = random.sample(archivos_wav, cantidad)

    if not os.path.exists(destino):
        os.makedirs(destino)

    for archivo in archivos_seleccionados:
        origen_path = os.path.join(carpetapath, archivo)
        destino_path = os.path.join(destino, archivo)
        shutil.copy(origen_path, destino_path)

    print(f"Se han seleccionado y guardado {cantidad} archivos .wav en la carpeta {destino}.")

carpeta = "C:/Users/Carlita/Desktop/tesis/Experiment 1 chunks/no_violence"  
carpeta_destino = "C:/Users/Carlita/Desktop/tesis/Experiment 2 chunks duration 9/no_violence"  
cantidad_archivos = 100

seleccionar_y_guardar_archivos(carpeta, carpeta_destino, cantidad_archivos)
