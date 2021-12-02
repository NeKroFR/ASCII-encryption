def encode (msg, key):
    while (len(key) < len(msg)):
        key += key
    encoded = ''
    for i in range (len(msg)):
        letter = ord(msg[i]) + ord(key[i])
        while letter > 1114112:
            letter -= 1114111
        encoded += chr(letter)
    return encoded

msg = str(input('message: '))
key = str(input('key: ')).replace(" ", "")
print(key)
encoded = encode(msg, key)
print(encoded)
file = open("encrypted.txt", "w").write(encoded)
