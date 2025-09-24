def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def main():
    path = '/home/dreadfarer/github.com/Dreadfarer/bookbot/books/frankenstein.txt'
    book_text=get_book_text(path)
    words = book_text.split()
    print(f'Found {len(words)} total words')

main()