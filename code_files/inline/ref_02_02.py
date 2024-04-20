import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def generate_and_print_password(length):
    # Generate a secure password of the specified length
    password = generate_password(length)
    print("Generated Password:", password)

generate_and_print_password(12)
