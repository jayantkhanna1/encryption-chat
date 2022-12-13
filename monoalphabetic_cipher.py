# Monoalphabetic Cipher

def encrypt(text,s):
    temp = {}
    for x in s:
        temp[x] = s.index(x)
    for x in text:
        if x in temp:
            text = text.replace(x,chr(temp[x]+65))
    return text

def decrypt(text,s):
    temp = {}
    for x in s:
        temp[x] = s.index(x)
    for x in text:
        if x in temp:
            text = text.replace(x,s[temp[x]])
    return text
