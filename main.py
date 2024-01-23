from pathlib import Path
def main():
    filePath = Path.cwd().joinpath('./books/frankenstein.txt')
    text = get_book_text(filePath)
    print(text)
    print(f'No of words = {get_book_word_count(filePath)}')
    
def get_book_text(bookpath):
    with open(bookpath) as f:
        return f.read()

def get_book_word_count(bookpath):
    text = get_book_text(bookpath)
    return len(text.split())
main()