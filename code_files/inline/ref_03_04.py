import hashlib

def calculate_checksum(data):
    return hashlib.md5(data.encode()).hexdigest(), hashlib.sha1(data.encode()).hexdigest(), hashlib.sha256(data.encode()).hexdigest()

def main():
    data = "Hello, world!"
    md5_hash, sha1_hash, sha256_hash = calculate_checksum(data)
    
    print("Data:", data)
    print("MD5 Checksum:", md5_hash)
    print("SHA1 Checksum:", sha1_hash)
    print("SHA256 Checksum:", sha256_hash)

if __name__ == "__main__":
    main()
