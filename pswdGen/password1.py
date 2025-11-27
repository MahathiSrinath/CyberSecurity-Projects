#Password Generator

import os
import base64

while True:
    try:
        bytes = input("Enter the number of  bytes of password to generate(1 and onwards): ")
        size = int(bytes) # converting str(number) to int(number)

        if size >= 1:#check if natural number
            break  #size validated
        else: #test for 0 and -ve values
            print("That's not a natural number. Please enter 1 or greater.")
    except ValueError: #in case of error
        print("Invalid input. Please enter a natural number.")


#returns a string which represents random bytes suitable for cryptographic use
crypt_password = os.urandom(size)
#converting cryptographical bytes into a password string
password_string = base64.urlsafe_b64encode(crypt_password).decode('utf-8')

"""Base64 encoding converts every 3 bytes into 4 characters.
The length of the password_string will be approximately (size / 3) * 4"""
print("Length of password generated: ",len(password_string))# Consider padding

print(f" Password Generated: {password_string}")

""" For generating secure passwords in Python,
  `os.urandom()` is highly recommended over the `random` module.
`random` module functions are pseudorandom, meaning they're predictable if their seed(algorithm/implementation details/working mechanism)
   is known,making them unsuitable for security.
In contrast, `os.urandom()` provides cryptographically secure random bytes by tapping into the
 operating system's true randomness (entropy) sources.
This ensures the generated passwords are highly unpredictable and resistant to guessing or prediction attacks,
 crucial for robust security."""

"""---
### Time Complexity

The time complexity is **$O(\text{size})$**. After input validation,
the core operations—generating random bytes, Base64 encoding, and decoding—all process data proportional to the
specified password `size`, leading to a linear increase in execution time.

---

### Space Complexity

The space complexity is also **$O(\text{size})$**.
This is because both the raw cryptographic bytes and the final
Base64-encoded password string occupy memory directly proportional to the `size`,
making memory usage scale linearly with the password's length."""





