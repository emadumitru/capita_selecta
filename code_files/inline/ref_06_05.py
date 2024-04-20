def tower_of_hanoi(n, source, auxiliary, target):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        tower_of_hanoi(n-1, source, target, auxiliary)
        
        # Move the nth disk from source to target peg
        print(f"Move disk {n} from {source} to {target}")
        
        # Move the n-1 disks from auxiliary peg to target peg
        tower_of_hanoi(n-1, auxiliary, source, target)

def solve_tower_of_hanoi(num_disks, source_peg, auxiliary_peg, target_peg):
    tower_of_hanoi(num_disks, source_peg, auxiliary_peg, target_peg)

# Define the number of disks and the pegs
num_disks = 3
source_peg = "A"
auxiliary_peg = "B"
target_peg = "C"

# Call the solve_tower_of_hanoi function
solve_tower_of_hanoi(num_disks, source_peg, auxiliary_peg, target_peg)