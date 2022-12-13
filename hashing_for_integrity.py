from passlib.hash import sha512_crypt as sha512
def encrypt(data,key):
    return sha512.hash(data, rounds=5000,salt=key)

def decrypt(data,key):
    return "Hash can not be decrypted"