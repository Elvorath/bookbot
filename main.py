from stats import get_num_words, get_char_arr, dict_to_arr

import sys

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    print("----------- Word Count ----------")
    frankenstein = get_book_text(sys.argv[1])
    num_words = get_num_words(frankenstein)
    print(f"Found {num_words} total words")

    print("----------- Character Count -----")
    char_arr = get_char_arr(frankenstein)
    sorted_arr = dict_to_arr(char_arr)
    for row in sorted_arr:
        print(f"{row.get("char")}: {row.get("count")}")
    print("============= END ===============")

main()
