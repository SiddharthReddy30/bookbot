from pathlib import Path
def main():
    filePath = Path.cwd().joinpath('./books/frankenstein.txt')
    text = get_book_text(filePath)
    print(text)
    
def get_book_text(bookpath):
    with open(bookpath) as f:
        return f.read()

main()