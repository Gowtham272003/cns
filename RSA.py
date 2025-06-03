import math

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c, d, n)



# Step 1: Key Generation
p = int(input("Enter p: "))
q = int(input("Enter q: "))
n = p * q            # n = 3233
phi = (p - 1) * (q - 1)  # phi = 3120
e = 17               # Public exponent

# Step 2: Compute Private Key d using pow()
if math.gcd(e, phi) != 1:
    raise ValueError("e and phi(n) are not coprime")
d = pow(e, -1, phi)  # Modular inverse

# Step 3: Encryption
m = 65  # Plaintext
c = encrypt(m, e, n)

# Step 4: Decryption
decrypted = decrypt(c, d, n)

# === Output ===
print("=== RSA Algorithm ===")
print(f"Prime p = {p}")
print(f"Prime q = {q}")
print(f"n = p * q = {n}")
print(f"φ(n) = {phi}")
print(f"Public key (e, n) = ({e}, {n})")
print(f"Private key (d, n) = ({d}, {n})")
print(f"\nPlaintext (m) = {m}")
print(f"Ciphertext (c = m^e mod n) = {c}")
print(f"Decrypted message (m = c^d mod n) = {decrypted}")
