import binascii
import string

def single_byte_xor(input_bytes, key):
    """XORs input bytes with a single-byte key."""
    return bytes([b ^ key for b in input_bytes])

def score_text(text):
    """Scores a text based on English letter frequency."""
    common_letters = "ETAOIN SHRDLU"
    score = sum([text.count(ch) for ch in common_letters.lower()])
    return score

def detect_xor_cipher(hex_strings):
    """Detects the single-character XOR encrypted string."""
    best_score = 0
    best_plaintext = None
    best_line = None
    
    for line in hex_strings:
        encrypted_bytes = binascii.unhexlify(line.strip())
        
        for key in range(256):
            decrypted = single_byte_xor(encrypted_bytes, key)
            
            try:
                decoded = decrypted.decode("ascii")  # Ensure it's readable ASCII
                score = score_text(decoded)
                
                if score > best_score:
                    best_score = score
                    best_plaintext = decoded
                    best_line = line.strip()
            except:
                continue  # Ignore invalid ASCII decodings
    
    return best_line, best_plaintext

# Read the file
with open("D:\\Cryptography practice\\set1\\file.txt", "r") as f:
    hex_strings = f.readlines()

# Detect the encrypted line
line, plaintext = detect_xor_cipher(hex_strings)

print("Encrypted Line:", line)
print("Decrypted Message:", plaintext)
