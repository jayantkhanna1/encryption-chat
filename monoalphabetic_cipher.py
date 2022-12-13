# Monoalphabetic Cipher

def encrypt(text,s):
    if text.isupper():
        text = text.lower()
    temp = {}
    for x in s:
        temp[x] = s.index(x)
    for x in text:
        if x in temp:
            text = text.replace(x,chr(temp[x]+65))
    return text

def decrypt(text,s):
    if text.islower():
        text = text.upper()
    temp = {}
    for x in s:
        temp[x] = s.index(x)
    for x in text:
        if x == " ":
            text = text.replace(x," ")
        else:
            val = ord(x)-65
            value = {i for i in temp if temp[i]==val}
            value = str(value)
            value = value.replace("{","")
            value = value.replace("}","")
            value = value.replace("'","")
            text = text.replace(x,value)
    return text
