from pydub import AudioSegment
import librosa
import soundfile as sf
import glob


def resample():

    WAV_FOLDER = "/Users/sharvitomar/Downloads/acoustic-distance-measure/Audio/german_wavs/"
    RESAMPLE_WAV_FOLDER = "/Users/sharvitomar/Downloads/acoustic-distance-measure/Audio/german_wavs_resampled/"

    all_wav_files = glob.glob(WAV_FOLDER + '*.wav')
    combined_sounds = AudioSegment.from_wav(all_wav_files[0])
    
    for i in range(1,len(all_wav_files)):
        combined_sounds = +AudioSegment.from_wav(all_wav_files[i])

    combined_sounds.export("/Users/sharvitomar/Downloads/acoustic-distance-measure/Audio/scottish_male/scottish.wav", format="wav")

def main():
    resample()

if __name__ == '__main__':
    main()