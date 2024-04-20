import hashlib

def calculate_checksum(data):
    md5_hash = hashlib.md5(data.encode()).hexdigest()
    sha1_hash = hashlib.sha1(data.encode()).hexdigest()
    sha256_hash = hashlib.sha256(data.encode()).hexdigest()
    
    return md5_hash, sha1_hash, sha256_hash

def print_checksums(data):
    md5_hash, sha1_hash, sha256_hash = calculate_checksum(data)
    
    print("Data:", data)
    print("MD5 Checksum:", md5_hash)
    print("SHA1 Checksum:", sha1_hash)
    print("SHA256 Checksum:", sha256_hash)

def main():
    data = "Hello, world!"
    print_checksums(data)

if __name__ == "__main__":
    main()