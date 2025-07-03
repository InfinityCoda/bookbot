

def get_num_words(text):
    # Create a list containing each word as an entry
    # then get its length to get the number of words
    split_text = text.split()
    num_words = len(split_text)
    #print(split_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def get_num_characters(text):
    # Get the count of each character in the text (including symbols/spaces)
    # upper/lowercase letters should be counted together
    # store the result as a dictionary with char as key & count (int) as value
    text = text.lower()
    char_counts = {}
    for char in text:
        if char not in char_counts: # each char needs to be initialized at 0
            char_counts[char] = 0
        char_counts[char] += 1
    #print(f"Characters found in the document: {char_counts}")
    return char_counts

def sort_on(items):
    return items["num"]

def sort_character_counts(char_counts):
    char_dicts = []
    for key, value in char_counts.items():
        #print(f"{key}: {value}")
        new_dict = {"char": key, "num": value}
        char_dicts.append(new_dict)
    char_dicts.sort(key=sort_on, reverse=True)
    print("--------- Character Count -------")
    for item in char_dicts:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
