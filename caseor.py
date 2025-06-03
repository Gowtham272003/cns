def encrypt(plain, shifts): 
    cipher = "" 
    for c in plain: 
        if c == " ": 
            cipher += " " 
        elif c.isupper(): 
            cipher += chr((ord(c) + shifts - 65) % 26 + 65) 
        elif c.islower(): 
            cipher += chr((ord(c) + shifts - 97) % 26 + 97) 
        elif c.isdigit(): 
            cipher += chr((ord(c) + shifts - 48) % 10 + 48) 
        else: 
            cipher += chr(ord(c) + shifts) 
    return cipher 

def decrypt(cipher, shifts): 
    plain = "" 
    for c in cipher: 
        if c == " ": 
            plain += " " 
        elif c.isupper(): 
            plain += chr((ord(c) - shifts - 65) % 26 + 65) 
        elif c.islower(): 
            plain += chr((ord(c) - shifts - 97) % 26 + 97) 
        elif c.isdigit(): 
            plain += chr((ord(c) - shifts - 48) % 10 + 48) 
        else: 
            plain += chr(ord(c) - shifts) 
    return plain 

# Main program
plain = input("Enter plain text: ") 
shifts = int(input("Enter shifts: ")) 
cipher = encrypt(plain, shifts) 
print("Encrypted text: " + cipher) 
print("Decrypted text: " + decrypt(cipher, shifts))
