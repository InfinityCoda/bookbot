from stats import *
import sys

def get_book_text(book_file):
    with open(book_file) as book:
        file_contents = book.read()
        return file_contents
    


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    book_text = get_book_text(sys.argv[1])
    get_num_words(book_text)
    char_count = get_num_characters(book_text)
    sort_character_counts(char_count)
    #print(book_text)

main()