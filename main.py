import sys
from stats import get_num_words
from stats import get_character_count
from stats import sorted_report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text(sys.argv[1])
    num_of_words = get_num_words(book_text)
    sorted_data = (sorted_report(get_character_count(book_text)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for item in sorted_data:
        char, count = list(item.items())[0]
        print(f"{char}: {count}")
main()