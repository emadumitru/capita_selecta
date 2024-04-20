import random

def generate_data():
    data = []
    for _ in range(10):
        data.append(random.randint(0, 100))
    return data

def calculate_sum(data):
    checksum = 0
    for num in data:
        checksum += num
    return checksum

def display_checksum(data, checksum):
    print("Data:", data)
    print("Checksum:", checksum)

def main():
    data = generate_data()
    checksum = calculate_sum(data)
    display_checksum(data, checksum)

if __name__ == "__main__":
    main()
