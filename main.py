def main():
    path = "books/frankenstein.txt"
    text = getBookText(path)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{getWordCount(text)} words found in the document")

#print(f"{getCharsToDict(text)}")
    charDict = getCharsToDict(text)
    for char,count in sorted(charDict.items(), key=lambda x: x[1], reverse=True):
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

def getBookText(path):
    with open(path) as book:
        return book.read()

def getWordCount(text):
    words = text.split()
    return (len(words))

def getCharsToDict(text):
    chars = {}
    for char in text:
        chars[char.lower()] = chars.get(char.lower(), 0) + 1
    return chars

main();