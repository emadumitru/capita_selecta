import random

def main():
    data = []
    checksum = 0
    for _ in range(10):
        num = random.randint(0, 100)
        data.append(num)
        checksum += num

    print("Data:", data)
    print("Checksum:", checksum)

if __name__ == "__main__":
    main()
