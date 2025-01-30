import string

LETTER_FREQUENCIES = {
    'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92,
    'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03,
    'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07
}

def xor_single_byte(ciphertext: bytes, key: int) -> bytes:
    return bytes([b ^ key for b in ciphertext])

def score_text(text: bytes) -> int:
    text_str = text.decode(errors="ignore").upper()  # Convert to uppercase for case-insensitive comparison
    return sum(LETTER_FREQUENCIES.get(char, 0) for char in text_str)

def single_byte_xor_crack(hex_str: str):
    ciphertext = bytes.fromhex(hex_str)
    best_score = 0
    best_plaintext = b"" #byte string
    best_key = None

    for key in range(256):
        decrypted = xor_single_byte(ciphertext, key)
        if all(chr(c) in string.printable for c in decrypted):  # Ignore non-printable results
            score = score_text(decrypted)
            if score > best_score:
                best_score = score
                best_plaintext = decrypted
                best_key = key

    return best_plaintext.decode(), best_key

# Given hex-encoded string
hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

plaintext, key = single_byte_xor_crack(hex_str)

print(f"Decrypted Message: {plaintext}")
print(f"Single-byte Key: {chr(key)} ({key})")
