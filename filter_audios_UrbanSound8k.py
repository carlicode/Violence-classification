import os
import shutil

def filter_files(input_folder, output_folder):
    # Verificar si la carpeta de salida existe, si no, crearla
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Recorrer los archivos de la carpeta de entrada
    for archivo in os.listdir(input_folder):
        ruta_archivo = os.path.join(input_folder, archivo)
        if os.path.isfile(ruta_archivo):
            nombre_archivo, extension = os.path.splitext(archivo)
            partes_nombre = nombre_archivo.split("-")
            if len(partes_nombre) == 4 and partes_nombre[1] == "0":
                # Mover el archivo a la carpeta de salida
                ruta_salida = os.path.join(output_folder, archivo)
                shutil.copyfile(ruta_archivo, ruta_salida)
                print(f"Archivo guardado: {ruta_salida}")

if __name__ == "__main__":
    input_folder = "C:/Users/Carlita/Desktop/tesis/dataset/Audios/No Violence/UrbanSound8K/fold10"
    output_folder = "C:/Users/Carlita/Desktop/tesis/dataset/Audios/No Violence/UrbanSound8K/10 air_conditioner"
    filter_files(input_folder, output_folder)
