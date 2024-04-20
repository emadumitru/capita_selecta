### Type: Checksum calculator --- Style: Rigorous

import hashlib

def calculate_checksum(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))
    return md5_hash.hexdigest()

def main():
    data = "Hello, world!"
    checksum = calculate_checksum(data)
    print("Checksum:", checksum)

if __name__ == "__main__":
    main()