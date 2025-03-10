import sys
from stats import get_num_words, get_chars_dict, sort_dict_to_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(filepath, word_count, chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in chars_list:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")

    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    number_of_words = get_num_words(get_book_text(filepath))
    chars_list = sort_dict_to_list(get_chars_dict(get_book_text(filepath)))
    print_report(filepath, number_of_words, chars_list)


main()
