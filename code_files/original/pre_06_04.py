### Type: Tower of Hanoi Problem --- Style: Modular

def tower_of_hanoi(n, source, auxiliary, destination):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        tower_of_hanoi(n-1, source, destination, auxiliary)
        
        # Move the nth disk from source to destination peg
        print(f"Move disk {n} from {source} to {destination}")
        
        # Move the n-1 disks from auxiliary to destination peg
        tower_of_hanoi(n-1, auxiliary, source, destination)

def main():
    num_disks = 3
    source_peg = "A"
    auxiliary_peg = "B"
    destination_peg = "C"
    
    print(f"Solving Tower of Hanoi problem with {num_disks} disks...")
    tower_of_hanoi(num_disks, source_peg, auxiliary_peg, destination_peg)
    print("Tower of Hanoi problem solved!")

if __name__ == "__main__":
    main()