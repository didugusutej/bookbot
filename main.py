
import sys
from stats import *

def main():
    #print(sys.argv[1])

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        words_count = word_count(text)
    
        char_count_dict = char_count(text)
    
        char_count_dict_sorted = sorted_dictionary(char_count_dict)
        #print(char_count_dict_sorted)
        print_report(book_path,words_count,char_count_dict_sorted)
    

    
    



def get_book_text(book):
    with open(book) as b:
        book_contents = b.read()
    return book_contents

def print_report(book_path,words_count, char_count_dict_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for item in char_count_dict_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()