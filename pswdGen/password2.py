#password generator
#Using the random module
import random
import string

#Generates a random password of the specified length.
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    if length < 1:
        return "\nPassword length must be at least 1."

    # Generate the password by randomly choosing characters
    password = ''.join(random.choice(characters) for i in range(length))

    return password


# Prompt the user for input and generate the password directly
try:
    desired_length = int(input("Enter the desired password length: "))
    new_password = generate_password(desired_length)
    print("Password Generated:", new_password)
except ValueError:
    print("Invalid input. Please enter a valid integer for the password length.")

"""
Time Complexity: O(length)

The time required to generate the password scales linearly with the desired password length.
A longer password means more random character selections and string concatenations.

Space Complexity: O(length)

The memory used by the algorithm also scales linearly with the desired password length,
primarily due to storing the generated password string in memory.
"""
