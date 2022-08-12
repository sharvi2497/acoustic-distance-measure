import glob
import librosa
from scipy.io import wavfile
import soundfile as sf


def resample():
    WAV_FOLDER = "/Users/sharvitomar/Downloads/acoustic-distance-measure/Audio/german_wavs/"
    RESAMPLE_WAV_FOLDER = "/Users/sharvitomar/Downloads/acoustic-distance-measure/Audio/german_wavs_resampled/"

    all_wav_files = glob.glob(WAV_FOLDER + '*.wav')

    for i in range(len(all_wav_files)):
        y, s = librosa.load(all_wav_files[i], mono= True, sr=16000) # Resample to 16kHz

        wav_file_name = all_wav_files[i].split("/")[-1]  # gives the names of wav files e.g. german1.wav
        desired_resampled_file_path = RESAMPLE_WAV_FOLDER + wav_file_name
        sf.write(desired_resampled_file_path, y, s)

def main():
    resample()

if __name__ == '__main__':
    main()