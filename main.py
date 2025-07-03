from stats import *

def get_book_text():
    with open("./books/frankenstein.txt") as frankenstein:
        file_contents = frankenstein.read()
        return file_contents
    


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book_text = get_book_text()
    get_num_words(book_text)
    char_count = get_num_characters(book_text)
    sort_character_counts(char_count)
    #print(book_text)

main()