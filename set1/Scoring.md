# Cryptographic Scoring Methods

In cryptography, **scoring** refers to the process of evaluating how likely a given piece of data (e.g., a decrypted message or a candidate key) is to be meaningful or correct. This is particularly useful in attacks like **brute-force**, **frequency analysis**, or **ciphertext-only attacks**, where you need to distinguish between random gibberish and valid plaintext.

## Scoring Methods in Cryptography

### **1. Frequency Analysis**
One of the most common scoring methods is based on **letter frequency**. In many languages, certain letters or combinations of letters appear more frequently than others. For example:
- In English, the most common letters are `E, T, A, O, I, N, S, H, R, D, L, C, U, M, W, F, G, Y, P, B, V, K, J, X, Q, Z`.
- Common bigrams (pairs of letters) include `TH, HE, IN, ER, AN, RE, ED, ON, ES, ST`.

#### **How It Works**:
- Compare the frequency of letters in the candidate plaintext to the known frequency distribution of the target language.
- Assign a score based on how closely the frequencies match.

#### **Example**:
```python
from collections import Counter

# Known frequency of letters in English (in percentage)
english_freq = {
    'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7,
    'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 6.7, 'j': 0.2,
    'k': 0.8, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5,
    'p': 1.9, 'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1,
    'u': 2.8, 'v': 1.0, 'w': 2.4, 'x': 0.2, 'y': 2.0,
    'z': 0.1
}

def frequency_score(text):
    """Score text based on how closely its letter frequencies match English."""
    text = text.lower()
    text_freq = Counter(text)
    total = sum(text_freq.values())
    
    # Calculate the frequency of each letter in the text
    text_freq = {char: (count / total) * 100 for char, count in text_freq.items()}
    
    # Compare to English frequencies
    score = 0
    for char in text_freq:
        if char in english_freq:
            score += abs(text_freq[char] - english_freq[char])
        else:
            score += 100  # Penalize non-alphabetic characters
    return score

# Example usage
text = "This is a sample text."
print(frequency_score(text))  # Lower score means closer to English
```

### **2. Dictionary-Based Scoring**
This method checks how many words in the candidate plaintext appear in a predefined dictionary of valid words.

#### **How It Works**:
- Split the candidate plaintext into words.
- Count how many words are in the dictionary.
- Assign a score based on the number of valid words.

#### **Example**:
```python
def dictionary_score(text, dictionary):
    """Score text based on how many words are in a dictionary."""
    words = text.lower().split()
    valid_words = sum(1 for word in words if word in dictionary)
    return valid_words / len(words) if words else 0

# Example usage
dictionary = {"this", "is", "a", "sample", "text"}
text = "This is a sample text."
print(dictionary_score(text, dictionary))  # Higher score means more valid words
```

### **3. Chi-Squared Statistic**
The Chi-squared test is a statistical method to compare observed frequencies with expected frequencies.

#### **How It Works**:
- Calculate the Chi-squared statistic for the candidate plaintext using the expected letter frequencies of the target language.
- A lower Chi-squared value indicates a better match.

#### **Example**:
```python
def chi_squared_score(text, expected_freq):
    """Calculate the Chi-squared statistic for the text."""
    text = text.lower()
    observed_freq = Counter(text)
    total = sum(observed_freq.values())
    
    chi_squared = 0
    for char in expected_freq:
        observed = observed_freq.get(char, 0)
        expected = expected_freq[char] * total / 100
        chi_squared += ((observed - expected) ** 2) / expected
    return chi_squared

# Example usage
text = "This is a sample text."
print(chi_squared_score(text, english_freq))  # Lower score means closer to English
```

### **4. N-Gram Analysis**
N-grams are sequences of `n` characters or words. For example, bigrams (2-grams) are pairs of letters like `TH`, `HE`, etc.

#### **How It Works**:
- Compare the frequency of n-grams in the candidate plaintext to the known frequency of n-grams in the target language.
- Assign a score based on how closely the frequencies match.

#### **Example**:
```python
from collections import defaultdict

# Precomputed bigram frequencies for English
english_bigrams = {
    'th': 1.52, 'he': 1.28, 'in': 0.94, 'er': 0.94, 'an': 0.82,
    're': 0.68, 'nd': 0.63, 'at': 0.59, 'on': 0.57, 'nt': 0.56,
    # Add more bigrams as needed
}

def bigram_score(text):
    """Score text based on bigram frequencies."""
    text = text.lower()
    bigrams = [text[i:i+2] for i in range(len(text)-1)]
    bigram_freq = Counter(bigrams)
    total = sum(bigram_freq.values())
    
    score = 0
    for bigram in bigram_freq:
        if bigram in english_bigrams:
            score += abs((bigram_freq[bigram] / total) * 100 - english_bigrams[bigram])
        else:
            score += 100  # Penalize unknown bigrams
    return score

# Example usage
text = "This is a sample text."
print(bigram_score(text))  # Lower score means closer to English
```

## **When to Use Scoring**:
- **Brute-Force Attacks**: To identify the correct key or plaintext among many candidates.
- **Ciphertext-Only Attacks**: To guess the encryption method or key.
- **Frequency Analysis**: To break substitution or transposition ciphers.
