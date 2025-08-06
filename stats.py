def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lower_text = text.lower()
    letter_count = {}
    for c in lower_text:
        if c in letter_count:
            letter_count[c] += 1
        else:
            letter_count[c] = 1
    return letter_count
        
def sort_on(d):
    return d["num"]


def sorted_dictionary(char_num_dict):
    sorted_list = []
    for char in char_num_dict:
        sorted_list.append({"char": char, "num":char_num_dict[char]})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

