import os
import csv
import numpy as np
from sentence_transformers import CrossEncoder

def text_labeling(text_folder, model_path, output_file):
    # Inicializar el modelo CrossEncoder
    model = CrossEncoder(model_path)

    # Obtener la lista de archivos de texto en la carpeta
    text_files = [f for f in os.listdir(text_folder) if f.endswith('.txt')]

    # Lista para almacenar los resultados
    results = []

    # Procesar cada archivo de texto
    for text_file in text_files:
        # Ruta completa del archivo de texto
        text_path = os.path.join(text_folder, text_file)
        
        # Obtener el nombre del archivo de audio (.wav)
        audio_name = os.path.splitext(text_file)[0] + '.wav'
        
        try:
            # Leer el contenido del archivo de texto
            with open(text_path, 'r') as file:
                text = file.read().strip()
        except:
            print(f"Error al leer el archivo de texto: {text_file}")
            continue
        
        # Pasar el texto por el modelo CrossEncoder
        scores = model.predict([(text, 'No violence'), (text, 'Violence'), (text, 'Neutral')])
        
        # Verificar que las puntuaciones tengan la dimensión adecuada
        if len(scores) != 3:
            print(f"Error en las puntuaciones para el archivo de texto: {text_file}")
            continue

        # Obtener la etiqueta y puntuación máxima
        max_score_idx = np.argmax(scores)
        label_mapping = ['no violence', 'violence', 'neutral']
        
        # Verificar si el índice está dentro del rango válido
        if max_score_idx < 0 or max_score_idx >= len(label_mapping):
            print(f"Índice de puntuación máxima fuera de rango para el archivo de texto: {text_file}")
            continue
        
        max_label = label_mapping[max_score_idx]
        max_score = scores[max_score_idx]
        
        # Guardar los resultados en la lista
        results.append([audio_name, text_file, max_label, max_score])
        
    # Guardar los resultados en un archivo CSV
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['audio_name', 'text_name', 'prediction_label', 'prediction_result'])
        writer.writerows(results)


if __name__ == '__main__':
    text_folder = 'C:/Users/Carlita/Desktop/tesis/dataset/30segundos/texts_chunks'
    model_path = 'cross-encoder/nli-deberta-base'
    output_file = 'C:/Users/Carlita/Desktop/tesis/dataset/30segundos/resultados.csv'

    text_labeling(text_folder, model_path, output_file)

