# Caesar Cipher

A command-line Caesar Cipher implementation in C that encrypts plaintext by shifting alphabetic characters using a numeric key provided as a command-line argument. Validates key input and preserves case and non-alphabetic characters.[web:41][web:43]

## What is Caesar Cipher?

Classic substitution cipher where each letter shifts a fixed number of positions in the alphabet. Named after Julius Caesar. Non-alphabetic characters (spaces, punctuation) remain unchanged.[web:41][web:42]

**Encryption Formula:**

Lowercase: (ch - 'a' + key) % 26 + 'a'
Uppercase: (ch - 'A' + key) % 26 + 'A'


## Features

- Command-line key argument (`./cipher 13`)
- Numeric key validation (all digits required)
- Preserves letter case (A-Z, a-z)
- Non-alphabetic characters unchanged
- CS50 library integration (`get_string`)
- Proper usage error handling

## Usage

1. **Compile:**
   make cipher
   or
   clang -o cipher cipher.c -lcs50

2. **Run with numeric key:**
  ./cipher 13

   **Sample Run:**
plaintext: Hello, World!
ciphertext: Uryyb, Jbeyq!

**Error Cases:**
$ ./cipher # Missing key
Usage: ./cipher key

$ ./cipher abc # Non-numeric key
Key must be numeric!

$ ./cipher 26 # Valid (26%% 26 = 0, no shift)
plaintext: ABC
ciphertext: ABC


## Complexity Analysis

- **Time Complexity:** O(n) where n = plaintext length[web:43]
- **Space Complexity:** O(1) - modifies input string in-place[web:43]

## Compilation Requirements

- CS50 library (`libcs50`)
- Standard C libraries (`stdio.h`, `stdlib.h`, `string.h`, `ctype.h`)


