import sys

def count_words_in_vtt(file_path):
    """
    Count the number of words in a VTT file.
    
    Args:
    - file_path (str): Path to the VTT file.
    
    Returns:
    - int: Number of words in the VTT file.
    """
    word_count = 0

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip lines with just numbers and timestamps
            if not line.isdigit() and '-->' not in line:
                word_count += len(line.split())

    return word_count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <path_to_vtt_file>")
        sys.exit(1)

    FILE_PATH = sys.argv[1]
    total_words = count_words_in_vtt(FILE_PATH)
    print(f"Total words in {FILE_PATH}: {total_words}")
