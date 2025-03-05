from stats import letterCount,charCount
import sys

#print("hello world")

def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    #print(get_book_text("books/frankenstein.txt"))
    with open(book) as f:
        file_content = f.read()
        #print(file_content)
        #print(charCount(file_content))
        #print(letterCount(file_content))
        report = letterCount(file_content)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book}...")
    print(f"----------- Word Count ----------")
    print(f"Found {charCount(file_content)} total words")
    print(f"--------- Character Count -------")
    #print(report)
    for i in sorted(report.keys(), key=report.get, reverse=True):
        print(f"{i}: {report[i]}")
    print("============= END ===============")

main()
