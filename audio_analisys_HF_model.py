import os
import csv
from transformers import pipeline

def classify_texts_in_folder(text_folder, text_folder_output, output_filename):
    classifier = pipeline("zero-shot-classification", model='cross-encoder/nli-deberta-base')
    candidate_labels = ["violence", "neutral", "no violence"]

    text_files = [f for f in os.listdir(text_folder) if f.endswith('.txt')]

    results = []

    for text_file in text_files:
        text_path = os.path.join(text_folder, text_file)
        
        try:
            with open(text_path, 'r') as file:
                text = file.read().strip()
        except:
            print(f"Error al leer el archivo de texto: {text_file}")
            continue

        res = classifier(text, candidate_labels)
        scores = res['scores']
        results.append([text, text_file, scores])

    if not os.path.exists(text_folder_output):
        os.makedirs(text_folder_output)

    output_file = os.path.join(text_folder_output, output_filename)

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['text', 'text file', 'scores'])
        writer.writerows(results)

if __name__ == '__main__':
    text_folder = 'C:/Users/Carlita/Desktop/tesis/dataset/30segundos/texts_chunks'
    text_folder_output = 'C:/Users/Carlita/Desktop/tesis/dataset/30segundos'
    output_filename = 'resultado.csv'
    classify_texts_in_folder(text_folder, text_folder_output, output_filename)
