import sys
from stats import get_num_words, get_char_count
from stats import chars_dict_to_sorted_list




def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path: str, word_count: int, char_list: list[tuple[str,int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_list:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    char_count = get_char_count(book_text)
    char_count_list = chars_dict_to_sorted_list(char_count)
    print_report(book_path, word_count, char_count_list)

main()
