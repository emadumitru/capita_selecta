def tower_of_hanoi(n, source, auxiliary, destination):
    if n > 0:
        tower_of_hanoi(n-1, source, destination, auxiliary)
        print(f"Move disk {n} from {source} to {destination}")
        tower_of_hanoi(n-1, auxiliary, source, destination)

def move_disk(n, source, auxiliary, destination):
    if n > 0:
        move_disk(n-1, source, destination, auxiliary)
        print(f"Complex move disk {n} from {source} to {destination}")
        move_disk(n-1, auxiliary, source, destination)

def complex_tower_of_hanoi(n):
    print("Initializing complex Tower of Hanoi...")
    move_disk(n, "A", "B", "C")
    print("Complex Tower of Hanoi completed!")

# Main program
if __name__ == "__main__":
    n = 3  # Number of disks
    print(f"Solving Tower of Hanoi with {n} disks...")
    tower_of_hanoi(n, "A", "B", "C")
    print("Tower of Hanoi solved!")

    print("\n")

    print(f"Solving Complex Tower of Hanoi with {n} disks...")
    complex_tower_of_hanoi(n)
    print("Complex Tower of Hanoi solved!")