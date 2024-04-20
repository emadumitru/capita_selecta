import hashlib

def calculate_sha256_checksum(data):
    """
    Calculate the SHA256 checksum of the given data.
    """
    checksum = hashlib.sha256(data.encode()).hexdigest()
    return checksum

def generate_data():
    """
    Generate some sample data for checksum calculation.
    """
    data = "This is some sample data."
    return data

def main():
    """
    Main function to calculate and print the checksum.
    """
    data = generate_data()
    checksum = calculate_sha256_checksum(data)
    print("Checksum:", checksum)

if __name__ == "__main__":
    main()
