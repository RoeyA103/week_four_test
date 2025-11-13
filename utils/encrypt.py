def caesar_encrypt(text:str, offset:int):
    def helper(char,offset):
        limit = 26
        res = (ord(char) - 97 + offset) % limit
        return (chr(res + 97))
    new_text = ""
    for char in text:
        if char.isalpha():
            res = helper(char.lower() , offset)
            new_text += res
        else:
            new_text += char
    return new_text        

def caesar_decrypt(text:str, offset:int):
    def helper(char,offset):
        limit = 26
        res = (ord(char) - 97 - offset) % limit
        return (chr(res + 97))
    
    new_text = ""
    for char in text:
        if char.isalpha():
            res = helper(char.lower() , offset)
            new_text += res
        else:
            new_text += char
    return new_text 

def fence_encrypt(text):
    text = text.replace(" ", "")
    first = ""
    last = ""
    index = 0
    for index , char in enumerate(text):
        if index % 2 == 0:
            first += char
        else:
            last += char
    new_text = first + last

    return new_text 

def fence_decrypt(text):
    new_text = ""
    len_t = len(text) // 2
    for i in range(len_t):
        char1 = text[i]
        char2 = text[len_t+i]
        new_text += char1 + char2

    return new_text 




