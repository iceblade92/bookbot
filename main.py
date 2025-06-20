import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words
from stats import sort_letters



path = sys.argv[1]

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words()} total words")
    print("--------- Character Count -------")
    the_list = sort_letters()
    for char_data in the_list:
        print(f"{char_data["char"]}: {char_data["num"]}")
    print("============= END ===============")
if __name__ == "__main__":
    main()