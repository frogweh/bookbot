#print("hello world")
def charCount(book):
    return len(list(filter(None,list(book.replace("\n"," ").split(" ")))))

def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        #print(type(file_content))
        #print(file_content)
        print(charCount(file_content))

main()
