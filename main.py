#print("hello world")
def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print(type(file_content))
        #print(file_content)

main()
