from stats import  num_words_in_file,character_frequency
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    file_content = get_book_test(path_to_file)

    num_words = num_words_in_file(file_content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_freq = character_frequency(file_content)
    print("--------- Character Count -------")

    for char, count in char_freq.items():
        print(f"{char}: {count}")

    print("============= END ===============")



def get_book_test(file_path):
    file_content = ""
    with open(file_path) as f:
       file_content = f.read()

    return file_content


main()