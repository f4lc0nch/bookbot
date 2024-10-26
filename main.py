def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    #convert dictionary in list of dictonary
    chars_list = []
    for char, count in chars_dict.items():
        char_dict = {"char": char, "count": count}
        chars_list.append(char_dict)

    #Sort
    chars_list.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    #get the "var" and print it
    for char_dict in chars_list:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text.lower():
        if c.isalpha():
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
