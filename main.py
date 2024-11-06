def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_dict_list = make_dict_list(chars_dict)
    chars_dict_list.sort(reverse=True, key=sort_on)
    report(book_path, num_words, chars_dict_list)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as file:
        return file.read()


def make_dict_list(dict):
    dict_to_list = []
    for c in dict:
        if c.isalpha():
            input_char = {"char": c, "num": dict[c]}
            dict_to_list.append(input_char)
    return dict_to_list


def sort_on(dict):
    return dict["num"]


def report(book_path, num_words, chars_dict_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for c in chars_dict_list:
        print(f"The '{c['char']}' character was found {c['num']} times")
    print("--- End report ---")



main()
