# Acoustic-based distance calculation

An acoustic-based method that can be used to calculate the distance between pronunciations.

## Requirements
 - Python 3.6
 - PRAAT 6.1.08
 - Hidden Markov Toolkit (HTK) 3.4
 - FAVE
 - R





## Usage

### 1: Audio
Keep the audio samples in `Audio`. A good data source: http://accent.gmu.edu/browse_language.php

1. The input audio must be in a .wav file format. Resample all audio files to 16 KHz mono PCM for calculating distance between the pronunciation. Run `resample.py`
2. Maintain a transcript file in .txt format that contains all the words spoken in the audio samples.

### 1: Forced-alignment
**Input:** audio files

**Output:** aligned .TextGrid files

    Forced-alignment

Forced-alignment is introduced to capture the words present inside the audio files.
The [Penn Phonetics Lab Forced Aligner](https://babel.ling.upenn.edu/phonetics/old_website_2015/p2fa/index.html) is used to accomplish the task of forced-alignment.

1. Run alignment: `run_align.py`
2. Segment paragraphs into words: `wav_splitter.py`. This files extract start and end of words and segments the audio file into small .wav files with the audio for each word in the transcript separated.

### 2: MFCC generation
Generate MFCCs.

    MFCC

1. Generate MFCCs: `HCopy -T 1 -C config -S mfc_map.scp` Using `config.txt` with HTK parameters. 
2. HTK compressed format should be exported: `export_hlist.py`


### 3: Acoustic-based distance calculation
Distances are calculated using Dynamic Time Warping.

    DTW

1. `find_dtw.py` computes the distances (includes normalization).
