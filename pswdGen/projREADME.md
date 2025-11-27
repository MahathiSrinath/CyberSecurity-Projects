# OS Entropy Password Generator

A minimal, secure Python CLI tool that generates cryptographically strong passwords by tapping into the operating system's entropy pool using `os.urandom()`, encoding the result as URL-safe Base64 strings. Ideal for generating real-world credentials, API keys, and tokens.

## Why Use OS Entropy Instead of Python's `random` Module?

Python’s built-in `random` module uses a deterministic pseudo-random number generator (PRNG) which is fine for simulations and games but **not** safe for security-sensitive uses like password generation. If the seed or internal state is exposed, an attacker can predict future values.

This project uses `os.urandom()`, which draws random bytes directly from the OS-level entropy sources (e.g., hardware events), making the outputs cryptographically secure and highly unpredictable.

| Feature         | `random` module                   | `os.urandom()` (This project)          |
|-----------------|---------------------------------|---------------------------------------|
| Randomness Type | Deterministic PRNG (seedable)   | True OS entropy                       |
| Security Use    | Not recommended for secrets     | Cryptographically secure              |
| Predictability | Can be predicted if seeded       | Highly unpredictable                  |
| Use Cases      | Games, simulations              | Passwords, tokens, cryptographic keys |

## Features

- User inputs the number of random bytes (≥ 1) to generate.
- Generates cryptographically secure random bytes using the OS entropy source.
- Encodes bytes into URL-safe Base64 for readability and usability.
- Input validation ensures natural numbers.
- Prints password length (approximately `(size / 3) * 4` characters due to Base64).

## Usage

1. Save the script as `secure_password_gen.py`.
2. Run it with Python 3.x:

python secure_password_gen.py

3. Enter the number of bytes for your password when prompted:

Example:
Enter the number of bytes of password to generate(1 and onwards): 16
Length of password generated: 24
Password Generated: 9ZbORysuQZNUlc0WiO7qhQ==

## Complexity

- **Time complexity:** O(n) — Random byte generation and Base64 encoding time grows linearly with requested size.
- **Space complexity:** O(n) — Memory usage is proportional to the byte size and encoded string length.

## Security Notes

- Uses OS entropy source, making it cryptographically strong and suitable for password/token generation.
- Avoid storing or logging generated passwords.
- Base64 encoding is URL-safe and eliminates potentially unsafe characters.
- For higher-level use cases, Python’s `secrets` module offers similar security built on `os.urandom()`.

## When to Use

Use this generator for secure password creation, API tokens, or any cryptographically sensitive key generation. For casual randomness without strict security needs, Python's `random` module remains useful.



