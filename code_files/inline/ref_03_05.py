import hashlib

def main():
    """
    Main function to calculate and print the checksum.
    """
    data = "This is some sample data."
    checksum = hashlib.sha256(data.encode()).hexdigest()
    print("Checksum:", checksum)

if __name__ == "__main__":
    main()
