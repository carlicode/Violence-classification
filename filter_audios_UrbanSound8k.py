import os
import shutil

def filter_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for archivo in os.listdir(input_folder):
        ruta_archivo = os.path.join(input_folder, archivo)
        if os.path.isfile(ruta_archivo):
            nombre_archivo, extension = os.path.splitext(archivo)
            partes_nombre = nombre_archivo.split("-")
            if len(partes_nombre) == 4 and partes_nombre[1] == "6":
                ruta_salida = os.path.join(output_folder, archivo)
                shutil.copyfile(ruta_archivo, ruta_salida)
                print(f"Archivo guardado: {ruta_salida}")

if __name__ == "__main__":
    for i in range(1,10):
        input_folder = "C:/Users/Carlita/Desktop/tesis/Dataset collection/UrbanSound8K/fold" + str(i) 
        output_folder = "C:/Users/Carlita/Desktop/tesis/Dataset collection/UrbanSound8K/6 gun"
        filter_files(input_folder, output_folder)
