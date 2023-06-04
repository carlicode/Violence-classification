import os
import csv
from sentence_transformers import CrossEncoder

def text_labeling(text_folder, model_path, output_file):
    model = CrossEncoder(model_path)
    text_files = [f for f in os.listdir(text_folder) if f.endswith('.txt')]
    results = []

    for text_file in text_files:
        text_path = os.path.join(text_folder, text_file)
        audio_name = os.path.splitext(text_file)[0] + '.wav'

        with open(text_path, 'r') as file:
            text = file.read().strip()
        scores = model.predict([(text, 'No violence'), (text, 'Violence'), (text, 'Neutral')])
        label_mapping = ['violence', 'no violence', 'neutral']
        labels = [label_mapping[score_max] for score_max in scores.argmax(axis=1)]
        max_label = max(labels, key=labels.count)
        results.append([audio_name, text_file, max_label, max(scores)])

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['audio_name', 'text_name', 'prediction_label', 'prediction_result'])
        writer.writerows(results)


if __name__ == '__main__':
    text_folder = 'C:/Users/Carlita/Desktop/tesis/dataset/30segundos/texts_chunks'
    model_path = 'cross-encoder/nli-deberta-base'
    output_file = 'C:/Users/Carlita/Desktop/tesis/dataset/30segundos/resultados.csv'

    text_labeling(text_folder, model_path, output_file)

