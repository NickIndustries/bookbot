def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_dict_to_list(dict):
    dict_list = []
    for char, count in dict.items():
        if char.isalpha():
            dict_list.append({"char": char, "count": count})
    def sort_on(dict):
        return dict["count"]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

