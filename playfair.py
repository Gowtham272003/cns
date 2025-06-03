def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix, seen = [], set()
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen and char.isalpha():
            matrix.append(char)
            seen.add(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs

def encrypt_digraph(matrix, a, b):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)

    if r1 == r2:
        # Same row: shift right
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:
        # Same column: shift down
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    else:
        # Rectangle rule: swap columns
        return matrix[r1][c2] + matrix[r2][c1]

def encrypt(text, key):
    matrix = generate_matrix(key)
    pairs = prepare_text(text)
    return "".join(encrypt_digraph(matrix, a, b) for a, b in pairs)

# Main
key = input("Enter Key: ")
plaintext = input("Enter plain text: ")
encrypted_text = encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)
