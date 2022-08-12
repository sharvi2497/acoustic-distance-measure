import glob
import os

def get_all_mfc_files(path):
    return glob.glob(path + '*.mfc')

def mfc_to_mfcc(mfc_paths, desired_mfcx_path):
    for mfc_path in mfc_paths:
        mfcx_file_name = mfc_path.split('/')[-1][:-4]
        desired_mfcx_full_path = desired_mfcx_path + mfcx_file_name + '.mfcx'
        os.system(f"HList -r {mfc_path} > {desired_mfcx_full_path}")

def main():
    # Provide wav folder path
    WAV_FOLDER = "/Users/sharvitomar/Downloads/acoustic-distance-measure/Audio/german_female_speakers/german_wavs_resampled/"
    all_files = glob.glob(WAV_FOLDER + '*.wav')
    for file in all_files:
        file_name = file.split("/")[-1][:-4]

        # Desired mfcx folder path and mfc files path
        os.mkdir('/Users/sharvitomar/Downloads/acoustic-distance-measure/Audio/german_mfcx_files/' + file_name)
        DESIRED_MFCX_PATH = "/Users/sharvitomar/Downloads/acoustic-distance-measure/Audio/german_mfcx_files/" + file_name + "/"
        MFC_PATH = "/Users/sharvitomar/Downloads/acoustic-distance-measure/Audio/german_mfc_files/" + file_name + "/"
        
        mfc_paths = get_all_mfc_files(MFC_PATH)
        mfc_to_mfcc(mfc_paths, DESIRED_MFCX_PATH)
        

if __name__ == '__main__':
    main()