from pathlib import Path
def main():
    filePath = Path.cwd().joinpath('./books/frankenstein.txt')
    text = get_book_text(filePath)
    print(text)
    print(f'No of words = {get_book_word_count(text)}')
    print(f'Alphabet count = {str(get_alphabets_count(text))}')

def get_book_text(bookpath):
    with open(bookpath) as f:
        return f.read()

def get_book_word_count(text):
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

main()