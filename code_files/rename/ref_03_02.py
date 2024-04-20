import hashlib

def calculate_checksums(data):
    md5_hash = hashlib.md5()
    sha1_hash = hashlib.sha1()
    sha256_hash = hashlib.sha256()

    md5_hash.update(data.encode())
    sha1_hash.update(data.encode())
    sha256_hash.update(data.encode())

    md5_checksum = md5_hash.hexdigest()
    sha1_checksum = sha1_hash.hexdigest()
    sha256_checksum = sha256_hash.hexdigest()

    return md5_checksum, sha1_checksum, sha256_checksum

def main():
    data = "Hello, world!"

    md5_checksum, sha1_checksum, sha256_checksum = calculate_checksums(data)

    print("Data:", data)
    print("MD5 Checksum:", md5_checksum)
    print("SHA1 Checksum:", sha1_checksum)
    print("SHA256 Checksum:", sha256_checksum)

if __name__ == "__main__":
    main()
