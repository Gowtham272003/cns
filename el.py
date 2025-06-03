import random
from sympy import isprime, mod_inverse

# Generate a large prime number
def generate_large_prime(bits=16):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

# Key generation
def generate_keys():
    p = generate_large_prime()
    g = random.randint(2, p - 2)
    x = random.randint(1, p - 2)  # Private key
    y = pow(g, x, p)              # y = g^x mod p
    public_key = (p, g, y)
    private_key = x
    return public_key, private_key

# Encryption
def encrypt(public_key, plaintext):
    p, g, y = public_key
    k = random.randint(1, p - 2)
    a = pow(g, k, p)
    s = pow(y, k, p)
    b = (plaintext * s) % p
    return (a, b)

# Decryption
def decrypt(private_key, public_key, ciphertext):
    p, g, y = public_key
    a, b = ciphertext
    s = pow(a, private_key, p)
    s_inv = mod_inverse(s, p)
    original = (b * s_inv) % p
    return original

# Main Program
if __name__ == "__main__":
    public_key, private_key = generate_keys()

    print("Public Key (p, g, y):", public_key)
    print("Private Key (x):", private_key)

    message = int(input("Enter a number to encrypt (e.g., 1–100): "))
    cipher = encrypt(public_key, message)
    print("Encrypted Cipher (a, b):", cipher)

    decrypted = decrypt(private_key, public_key, cipher)
    print("Decrypted Message:", decrypted)
