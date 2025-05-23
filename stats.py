
# takes a string and returns the number of words
def word_count(text):
    words = text.split()
    return len(words)

# takes a string and returns a dictionary with the number of times each character appears
def char_count(text):
    char_num = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_num:
            char_num[char] += 1
        else:
            char_num[char] = 1
    return char_num

# takes a dictionary and returns a list of dictionaries with the character and its count
# needed for sorted_dict
def sort_on(dict):
    return dict["num"]

# takes a dictionary and returns a list of dictionaries with the character and its count
# removes non-alphabetic characters and sorts the list in descending order based on the count
def sorted_dict(char_num):
    value_list = []
    for key, value in char_num.items():
        if key.isalpha():
            value_list.append({"char": key, "num": value})
    value_list.sort(reverse=True, key=sort_on)
    return value_list