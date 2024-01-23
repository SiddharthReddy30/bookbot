from pathlib import Path
def main():
    book_path = 'books/frankenstein.txt'
    filePath = Path.cwd().joinpath(book_path)
    text = get_book_text(filePath)
    print(text)
    print(f'No of words = {get_book_word_count(text)}')
    print(f'Alphabet count = {str(get_alphabets_count(text))}')
    generate_report(book_path, text)
def get_book_text(bookpath: Path):
    with open(bookpath) as f:
        return f.read()

def get_book_word_count(text: str):
    return len(text.split())

def get_alphabets_count(text: str):
    alphabet_count = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter in alphabet_count:
            alphabet_count[lower_letter] += 1
        else:
            alphabet_count[lower_letter]=1
    return alphabet_count

def generate_report(book_path: str, booktext: str):
    print(f'--- Begin report of {book_path} ---')
    print(f'{get_book_word_count(booktext)} words found in the document\n')
    sorted_dict = dict(sorted(get_alphabets_count(booktext).items(),key= lambda x:x[1],reverse=True))
    for letter,count in sorted_dict.items():
        if letter.isalpha():
            print(f'The \'{letter}\' character was found {count} times')
    print('-- End report --')

main()