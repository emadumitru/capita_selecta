import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = 12
    password = generate_password(password_length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()