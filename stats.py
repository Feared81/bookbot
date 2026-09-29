def get_num_words(book_text: str) -> int:
    words = book_text.split()
    return len(words)

def get_char_count(book_text: str) -> dict[str, int]:
    char_counter = {}
    for char in book_text.lower():
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    return char_counter

def sort_on(vehicle: tuple[str, int]) -> int:
    return vehicle[1]

def chars_dict_to_sorted_list(counts: dict[str, int]) -> list[tuple[str, int]]:
    counts_list = []
    for key, value in counts.items():
        counts_list.append((key,value))
    return sorted(counts_list, reverse=True, key=sort_on)
