
def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_num = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_num:
            char_num[char] += 1
        else:
            char_num[char] = 1
    return char_num

def sort_on(dict):
    return dict["num"]

def sorted_dict(char_num):
    value_list = []
    for key, value in char_num.items():
        if key.isalpha():
            value_list.append({"char": key, "num": value})
    value_list.sort(reverse=True, key=sort_on)
    return value_list