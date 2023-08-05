import os
import shutil

def filter_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for archivo in os.listdir(input_folder):
        ruta_archivo = os.path.join(input_folder, archivo)
        if os.path.isfile(ruta_archivo):
            nombre_archivo, extension = os.path.splitext(archivo)
            if nombre_archivo.endswith("-39"):
                ruta_salida = os.path.join(output_folder, archivo)
                shutil.copyfile(ruta_archivo, ruta_salida)
                print(f"Archivo guardado: {ruta_salida}")

if __name__ == "__main__":

    input_folder = "C:/Users/Carlita/Desktop/tesis/Dataset collection/ESC-50-master/audio"
    output_folder = "C:/Users/Carlita/Desktop/tesis/Experiment 2/glass breaking"
    filter_files(input_folder, output_folder)