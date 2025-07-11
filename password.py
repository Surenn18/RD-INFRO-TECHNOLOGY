import random
import string

def generate_password(length):
    if length < 4:
        return "Password should be at least 4 characters long."

    # Characters to include
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Ensure a mix of character types
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # Fill the rest with random characters
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the result
    random.shuffle(password)

    return ''.join(password)

# User Input
try:
    length = int(input("Enter desired password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
