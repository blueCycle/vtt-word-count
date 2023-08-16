# vtt-word-count

This program was created to work with raw transcript files obtained from the Zoom. It counts the number of words in a VTT (Web Video Text Tracks) file. Specifically, it's designed to skip lines containing timestamps, numeric identifiers, and any lines with just numbers, focusing solely on the actual content of the VTT file.

Prerequisites
Python 3.x

Usage
Clone the repository to your local machine:

git clone https://github.com/blueCycle/vtt-word-count.git
cd vtt-word-count

Run the script by passing the path to your VTT file as an argument:
python vtt-word-count.py path_to_vtt_file
