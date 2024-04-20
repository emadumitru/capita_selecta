import random
import string

def generate_secure_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    # Generate a secure password of length 12
    password = generate_secure_password(12)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
