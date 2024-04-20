import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def print_generated_password(length):
    # Generate a secure password of the specified length
    password = generate_password(length)
    print("Generated Password:", password)

def main():
    # Print a secure password of length 12
    print_generated_password(12)

if __name__ == "__main__":
    main()