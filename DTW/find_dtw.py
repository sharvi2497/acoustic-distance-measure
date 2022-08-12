from fastdtw import fastdtw

import glob
import numpy as np

def mfcx_to_numpy(file_name):
    with open(file_name,'r+') as f:
        lines = f.read().splitlines()
        embedding = ''.join(lines).split()
        embedding = [float(x) for x in embedding]
        return np.array(embedding)

def get_list_mfcx_files(file_path):
    return glob.glob(file_path + '*.mfcx')

def find_mean_dtw(file_path_speaker1, file_path_speaker2):
    sum_distance = 0
    speaker_1_mfcx_files = get_list_mfcx_files(file_path_speaker1)
    speaker_2_mfcx_files = get_list_mfcx_files(file_path_speaker2)
    euc_distance = lambda x, y: (x - y)**2

    for i in range(len(speaker_1_mfcx_files)):
        speaker_1_word_embedding = mfcx_to_numpy(speaker_1_mfcx_files[i])
        speaker_2_word_embedding = mfcx_to_numpy(speaker_2_mfcx_files[i])
        d, _ = fastdtw(speaker_1_word_embedding, speaker_2_word_embedding, dist=euc_distance)
        sum_distance += np.sqrt(d)/(len(speaker_1_mfcx_files[i])+len(speaker_2_mfcx_files[i]))
    
    return sum_distance


def main():

    # Give path of MFCS files folder 
    FILE_PATH_SPEAKER_1 = "/Users/sharvitomar/Downloads/acoustic-distance-measure/Audio/claudia/claudia_mfcx_files/"
    FILE_PATH_SPEAKER_2 = "/Users/sharvitomar/Downloads/acoustic-distance-measure/Audio/hindi4/hindi4_mfcx_files/"
    dtw = find_mean_dtw(FILE_PATH_SPEAKER_1, FILE_PATH_SPEAKER_2)) 
   
    print("Mean distance between the two speakers is: ", dtw)

if __name__ == '__main__':
    main()
