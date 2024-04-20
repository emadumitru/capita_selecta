import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_print_password(password_length):
    password = generate_password(password_length)
    print("Generated Password:", password)

generate_and_print_password(12)
