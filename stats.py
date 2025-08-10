def get_num_words(text):
    return len(text.split())

def get_char_arr(text):
    result = {}
    tmp = text.lower()
    for char in tmp:
        result[char] = result.get(char,0) + 1
    return result

def dict_to_arr(arr):
    result = []
    for key in arr.keys():
        if not key.isalpha(): continue
        result.append({"char": key, "count": arr.get(key)})
    result.sort(reverse=True, key=lambda row: row.get("count"))
    return result
