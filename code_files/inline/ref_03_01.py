import hashlib

def main():
    data = "Hello, world!"
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))
    checksum = md5_hash.hexdigest()
    print("Checksum:", checksum)

if __name__ == "__main__":
    main()
