import librosa

def audio_analysis(audio_path):
    # Cargar el archivo de audio
    audio, sr = librosa.load(audio_path)

    # Aplicar preénfasis
    audio_preemphasized = librosa.effects.preemphasis(audio)

    # Calcular el espectrograma de potencia
    spectrogram = librosa.feature.melspectrogram(y=audio_preemphasized, sr=sr)

    # Calcular los coeficientes MFCC
    mfcc = librosa.feature.mfcc(S=librosa.power_to_db(spectrogram), n_mfcc=13)

    # Extraer los aspectos
    aspecto_1 = librosa.feature.rms(audio)
    aspecto_2 = librosa.feature.zero_crossing_rate(audio)
    aspecto_3 = librosa.feature.spectral_centroid(S=spectrogram)
    aspecto_4 = librosa.feature.spectral_rolloff(S=spectrogram)
    aspecto_5 = librosa.feature.spectral_bandwidth(S=spectrogram)
    aspecto_6 = librosa.feature.chroma_stft(S=librosa.power_to_db(spectrogram), sr=sr)
    aspecto_7 = librosa.feature.poly_features(S=spectrogram, order=1)

    # Imprimir los resultados
    print("Aspecto 1 - RMS:", aspecto_1)
    print("Aspecto 2 - Zero Crossing Rate:", aspecto_2)
    print("Aspecto 3 - Spectral Centroid:", aspecto_3)
    print("Aspecto 4 - Spectral Rolloff:", aspecto_4)
    print("Aspecto 5 - Spectral Bandwidth:", aspecto_5)
    print("Aspecto 6 - Chroma STFT:", aspecto_6)
    print("Aspecto 7 - Poly Features:", aspecto_7)


if __name__ == "__main__":
    path = ''
    audio_analysis(path)
