def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input primes
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

if not (is_prime(p) and is_prime(q)):
    print("Both numbers must be prime.")
    exit()

# RSA Computation
n = p * q
phi = (p - 1) * (q - 1)

# Public key e
e = int(input(f"Enter public key e (1 < e < {phi}, and gcd(e, {phi}) = 1): "))
if gcd(e, phi) != 1:
    print("Invalid e. It must be coprime with φ(n).")
    exit()

# Private key d
d = mod_inverse(e, phi)

# Message input and encryption
msg = int(input(f"Enter number to encrypt (less than {n}): "))
cipher = pow(msg, e, n)
plain = pow(cipher, d, n)

# Output
print("\n--- RSA Keys ---")
print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

print("\n--- Results ---")
print("Encrypted:", cipher)
print("Decrypted:", plain)
