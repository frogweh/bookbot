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

