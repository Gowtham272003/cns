def extend_key(text, key):
    key = key.upper()
    return (key * (len(text) // len(key) + 1))[:len(text)]

def encrypt(plain, key):
    plain = plain.upper()
    key = extend_key(plain, key)
    cipher = ""

    for p, k in zip(plain, key):
        if p.isalpha():
            value = (ord(p) - ord('A') + ord(k) - ord('A')) % 26
            cipher += chr(value + ord('A'))
        else:
            cipher += p  # Keep non-alphabetic characters unchanged
    return cipher

def decrypt(cipher, key):
    cipher = cipher.upper()
    key = extend_key(cipher, key)
    plain = ""

    for c, k in zip(cipher, key):
        if c.isalpha():
            value = (ord(c) - ord('A') - (ord(k) - ord('A'))) % 26
            plain += chr(value + ord('A'))
        else:
            plain += c
    return plain

# Main
plain = input("Enter plain text: ")
key = input("Enter key: ")

cipher = encrypt(plain, key)
print("Encrypted text:", cipher)
print("Decrypted text:", decrypt(cipher, key))
