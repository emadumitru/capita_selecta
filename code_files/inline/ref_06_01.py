def tower_of_hanoi(n, source, auxiliary, destination):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        tower_of_hanoi(n-1, source, destination, auxiliary)
        
        # Move the nth disk from source to destination peg
        print(f"Move disk {n} from {source} to {destination}")
        
        # Move the n-1 disks from auxiliary peg to destination peg
        tower_of_hanoi(n-1, auxiliary, source, destination)

def solve_tower_of_hanoi(num_disks, source_peg, auxiliary_peg, destination_peg):
    tower_of_hanoi(num_disks, source_peg, auxiliary_peg, destination_peg)

# Number of disks
num_disks = 3

# Peg names
source_peg = "A"
auxiliary_peg = "B"
destination_peg = "C"

# Solve the Tower of Hanoi problem
solve_tower_of_hanoi(num_disks, source_peg, auxiliary_peg, destination_peg)