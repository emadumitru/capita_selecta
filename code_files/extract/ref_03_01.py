import hashlib

def calculate_checksum(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))
    return md5_hash.hexdigest()

def calculate_and_print_checksum(data):
    checksum = calculate_checksum(data)
    print("Checksum:", checksum)

def main():
    data = "Hello, world!"
    calculate_and_print_checksum(data)

if __name__ == "__main__":
    main()