import os
import csv

# Carpeta raíz que contiene las subcarpetas con los archivos .wav
carpeta_raiz = "C:/Users/Carlita/Desktop/tesis/Train model/data"

# Función para obtener el label de un archivo .wav
def obtener_label(nombre_archivo):
    # Elimina la extensión .wav y cualquier número al final del nombre
    nombre_sin_extension = os.path.splitext(nombre_archivo)[0]
    label = ''.join(filter(str.isalpha, nombre_sin_extension))
    return label

# Lista para almacenar las filas del CSV
filas_csv = []

# Recorre las carpetas y archivos .wav
for root, _, archivos in os.walk(carpeta_raiz):
    for archivo in archivos:
        if archivo.endswith(".wav"):
            # Obtiene el path completo del archivo
            path = os.path.join(root, archivo)
            # Obtiene el label
            label = obtener_label(archivo)
            # Agrega la fila al CSV
            filas_csv.append([path, label])

# Nombre del archivo CSV de salida
archivo_csv_salida = "C:/Users/Carlita/Desktop/tesis/Train model/data/audio_data.csv"

# Escribe los datos en el archivo CSV
with open(archivo_csv_salida, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Escribe el encabezado
    writer.writerow(["path", "label"])
    # Escribe las filas de datos
    writer.writerows(filas_csv)

print(f"Se ha creado el archivo CSV '{archivo_csv_salida}' con éxito.")
