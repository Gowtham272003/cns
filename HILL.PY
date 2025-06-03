def get_key_matrix(key):
    key_matrix = []
    k = 0
    for i in range(3):
        row = []
        for j in range(3):
            row.append(ord(key[k].upper()) - 65)
            k += 1
        key_matrix.append(row)
    return key_matrix

def multiply_matrix(matrix1, matrix2):
    result = [[0] for _ in range(3)]
    for i in range(3):
        for j in range(1):
            for k in range(3):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 26
    return result

def encrypt(message, key):
    key_matrix = get_key_matrix(key)
    msg_vector = [[ord(c.upper()) - 65] for c in message]
    cipher_vector = multiply_matrix(key_matrix, msg_vector)
    cipher_text = "".join(chr(num[0] + 65) for num in cipher_vector)
    return cipher_text

def mod_inverse_matrix(matrix, mod=26):
    import numpy as np
    det = int(round(np.linalg.det(matrix)))
    det = det % mod
    det_inv = pow(det, -1, mod)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    return (det_inv * adjugate) % mod

def decrypt(cipher_text, key):
    import numpy as np
    key_matrix = get_key_matrix(key)
    inv_matrix = mod_inverse_matrix(np.array(key_matrix), 26)
    cipher_vector = [[ord(c.upper()) - 65] for c in cipher_text]
    plain_vector = multiply_matrix(inv_matrix.tolist(), cipher_vector)
    plain_text = "".join(chr(num[0] + 65) for num in plain_vector)
    return plain_text

# Main program
message = input("Enter a 3-letter message: ").upper()
key = input("Enter a 9-letter key: ").upper()

if len(message) != 3 or len(key) != 9:
    print("Message must be 3 letters, and key must be 9 letters.")
else:
    encrypted = encrypt(message, key)
    print("Encrypted text:", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Decrypted text:", decrypted)
