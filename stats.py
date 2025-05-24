def num_words_in_file(file_content):
    return len(file_content.split())

def character_frequency(file_content):
    freq_counter = {}

    for char in file_content.lower():
        if char not in freq_counter:
            freq_counter[char]= 1
        else:
            freq_counter[char] += 1

    return freq_counter