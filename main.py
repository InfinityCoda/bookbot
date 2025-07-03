from stats import get_num_words

def get_book_text():
    with open("./books/frankenstein.txt") as frankenstein:
        file_contents = frankenstein.read()
        return file_contents
    


def main():
    book_text = get_book_text()
    get_num_words(book_text)
    #print(book_text)

main()