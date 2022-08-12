import logging
import glob
import os
from pydub import AudioSegment

def get_index_of_wav_start(textgrid_filename):
    with open(textgrid_filename,'r+') as f:
        lines = f.read().splitlines()
        for i, line in enumerate(lines):
            if line == '"word"':
                return i+6

def get_word_end_start(textgrid_filename, wav_start):
    words_list = []
    with open(textgrid_filename,'r+') as f:
        lines = f.read().splitlines()
        for i in range(wav_start, len(lines), 3):
            if lines[i] != '"sp"':
                word_list = []
                word_list.append(lines[i].replace('"', ''))
                word_list.append(float(lines[i-2]))
                word_list.append(float(lines[i-1]))
                words_list.append(word_list)
    return words_list

def split_and_save_wavfile(words_list, wavfilename, wavfilepath):
    os.mkdir('/german_segmented_wavs/'+ wavfilename) 
    for i in range(len(words_list)):
        start = words_list[i][1] * 1000
        end = words_list[i][2] * 1000
        target_audio = AudioSegment.from_wav(wavfilepath)
        target_segment = target_audio[start:end]
        # Provide output file path
        OUTPUT_FILENAME = '/german_segmented_wavs/'+ wavfilename+ "/" + wavfilename + '_' + str(i) + '_' + words_list[i][0] + '.wav'
        target_segment.export(OUTPUT_FILENAME, format="wav")

def create_mfc_map(words_list, wavfilename, hcopy_filename):
    file = open(hcopy_filename, 'w')
    os.mkdir('/german_mfc_files/' + wavfilename)
    for i in range(len(words_list)):
        start = words_list[i][1] * 1000 - 5
        end = words_list[i][2] * 1000 + 5

        # Provide MFC files and Wav file path names
        WAV_FILENAME = '/german_segmented_wavs/' + wavfilename+ "/" + wavfilename + '_' + str(i) + '_' + words_list[i][0] + '.wav'
        MFC_FILENAME = '/german_mfc_files/' + wavfilename+ "/" + wavfilename + '_' + str(i) + '_' + words_list[i][0] + '.mfc'
        file.write(WAV_FILENAME + ' ' + MFC_FILENAME + '\n')


def main():
    # Provide folder path of wav files
    WAV_FOLDER = "/german_wavs_resampled/"
    all_files = glob.glob(WAV_FOLDER + '*.wav')

    for file in all_files:
        file_name = file.split("/")[-1][:-4]

        # Provide path for mfc_map and textgrid files
        HCOPY_FILENAME = "/german_mfc_map/" + file_name + ".scp"
        TEXTGRID_FILENAME = "/german_textgrids/" + file_name + ".TextGrid"
        WAV_FILENAME = file_name
        WAV_FILEPATH = WAV_FOLDER + file_name +".wav"
        
        wav_start = get_index_of_wav_start(TEXTGRID_FILENAME)
        words_list = get_word_end_start(TEXTGRID_FILENAME, wav_start)
        split_and_save_wavfile(words_list, WAV_FILENAME, WAV_FILEPATH)
        create_mfc_map(words_list, WAV_FILENAME, HCOPY_FILENAME)

    

if __name__ == '__main__':
    main()