def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = word_count(text)
    print(f"{num_words} words found in the document")
    print(char_counts)
    char_list = [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()]

    char_list.sort (key= sort_on, reverse=True)
    
    for char_info in char_list:

        print(f"The '{char_info['char']}' character was found {char_info['num']} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(lower_string):
    word_dict = {}
    lower_string = lower_string.lower()
    for char in lower_string:
        if char in word_dict:
            word_dict[char] += 1
        else:
            word_dict[char] = 1
    
    return word_dict

def sort_on(word_dict):
    return word_dict["num"]






main()