import sys

path = sys.argv[1]
    
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def get_num_words():
    text = get_book_text(path)
    words = text.split()
    word_count = len(words)
    return word_count

def letter_counter():
    letters_counted = {}
    text = get_book_text(path)
    letter = text.lower()
    for i in letter:
        if i in letters_counted:
            letters_counted[i] = letters_counted[i] + 1
        else:
            letters_counted[i] = 1
    return letters_counted

def get_num_from_dict(item):
    value = item["num"]
    return value

def sort_letters():
    dict = letter_counter()
    list = []
    for key, value in dict.items():
        if key.isalpha():
            list.append({"char":key ,"num":value})
    list.sort(reverse=True, key=get_num_from_dict)
    return list
