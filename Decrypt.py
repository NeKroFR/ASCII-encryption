def decode (msg, key):
    while (len(key) < len(msg)):
        key += key
    decoded = ''
    for i in range (len(msg)):
        letter = ord(msg[i]) - ord(key[i])
        while letter < 0:
            letter += 1114111
        decoded += chr(letter)
    return decoded

f = open("encrypted.txt", "r")
msg = f.read()
key = str(input('key: ')).replace(" ", "")
print(key)
print(decode(msg, key))
