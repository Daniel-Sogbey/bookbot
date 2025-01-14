def main():
    content = read_file_content("books/frankenstein.txt")
    words_count = count_words(content)
    print(f"word count {words_count}")
    dict = characters_dict(content)
    printReport(dict)
    



def read_file_content(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words =  text.split()
    return len(words)

def characters_dict(text):
    dict = {}

    for character in text:
        lowered = character.lower()
        if lowered in  dict:
            dict[lowered] +=1
        else:
            dict[lowered] = 1
        
    return dict

def sort_on(dict):
    return dict["num"]

def printReport(dict):
    print("--- Begin report of books/frankenstein.txt ---")
    list = []

    for key in dict:
        if not key.isalpha():
            continue
        
        list.append({"char": key, "num": dict[key]})

    list.sort(reverse=True, key=sort_on)

    for item in list:
        print(f"The {item["char"]} character was found {item["num"]} times")


    print("--- End report ---")

main()