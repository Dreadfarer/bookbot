def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()
    
path = '/home/dreadfarer/github.com/Dreadfarer/bookbot/books/frankenstein.txt'
book_text=get_book_text(path)
words = book_text.split()

def count():
    print(f'Found {len(words)} total words')

def count_characters():
    dict = {}
    for word in words:
        lowered_char = word.lower()
        for char in lowered_char:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
    return dict