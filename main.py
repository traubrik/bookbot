def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print(f" ---Report for {book_path}--- ")
    print(f"{num_words} words found in the document")
    print()

    char_counts = count_characters(text)
    sorted_char_counts = sorted_chars(char_counts)

    for item in sorted_char_counts:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End of report ---")
    
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sorted_chars(char_counts):
    char_list = [{'char': char, 'count': count} for char, count in char_counts.items()]
    char_list.sort(key=lambda item: item['count'], reverse=True)
    return char_list


main()