def encode (msg, key):
    encoded = ''
    for i in range (len(msg)):
        letter = ord(msg[i]) + ord(key[i])
        encoded += chr(letter)
    return encoded

msg = str(input('message: '))
key = str(input('key: '))
encoded = encode(msg, key)
print(encoded)