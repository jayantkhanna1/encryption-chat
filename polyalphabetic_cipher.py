
def encrypt(text,key):
    chars = ' abcdefghijklmnopqrstuvwxyz'
    newText = ""
    for i in range(len(text)):
        targetIndex = chars.index(text[i]) + chars.index(key[i%len(key)])
        newText += chars[targetIndex%27]
	
    return newText

def decrypt(text,key):
    chars = ' abcdefghijklmnopqrstuvwxyz'
    newText = ""
    for i in range(len(text)):
        targetIndex = chars.index(text[i]) - chars.index(key[i%len(key)])
        newText += chars[targetIndex%27]
	
    return newText