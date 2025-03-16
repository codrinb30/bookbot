def get_num_words(book):
    num_of_words = len(book.split())
    return num_of_words

def get_character_count(book):
    ready_for_count = book.lower()
    char_dict = {}
    for char in ready_for_count:
        if char not in char_dict:
            char_dict[char] = 1
        elif char in char_dict:
            char_dict[char] += 1
    return char_dict

def sorted_report(char_count):
    sorted_list = []
    new_dict = {}
    for k, v in char_count.items():
        new_dict[k] = v
        if k.isalpha():
            sorted_list.append(new_dict)
        new_dict = {}
    sorted_list.sort(reverse=True, key=lambda d: list(d.values())[0])
    return sorted_list