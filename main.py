#print("hello world")
def charCount(book):
    return len(list(filter(None,list(book.replace("\n"," ").split(" ")))))

def letterCount(book):
    temp = {}
    for i in book:
        if not i.isalpha():
            continue
        letter = i.lower()
        if letter not in temp.keys():
            temp[letter] = 1
        else:
            temp[letter] += 1
    return temp

def main():
    print("greetings boots")
    return
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_content = f.read()
        #print(type(file_content))
        #print(file_content)
        #print(charCount(file_content))
        #print(letterCount(file_content))
        report = letterCount(file_content)
    print(f"--- Being report of {book} ---")
    print(f"{charCount(file_content)} words found in the document\n")
    for i in sorted(report.keys(), key=report.get, reverse=True):
        print(f"The {repr(i)} character was found {report[i]} times")
    print("--- End report ---")

main()
