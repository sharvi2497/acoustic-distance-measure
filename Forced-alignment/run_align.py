import glob
import os

def get_all_files(path):
    return glob.glob(path + '*.wav')

def main():
    # Provide wav folder path
    WAV_FOLDER = "/german_female_speakers/german_wavs_resampled/"
    all_files = get_all_files(WAV_FOLDER)

    for file in all_files:
        file_name = file.split("/")[-1][:-4]
        print(f'processing for file {file_name}')

        # Command below is "python align.py wavfile trsfile output_file"
        os.system(f'python /p2fa/align.py {file} /Audio/transcript.txt /Audio/german_textgrids/{file_name}.TextGrid')

if __name__ == "__main__":
    main()
