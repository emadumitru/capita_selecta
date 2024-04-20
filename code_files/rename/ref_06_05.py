def move_disks(n, source, auxiliary, target):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        move_disks(n-1, source, target, auxiliary)
        
        # Move the nth disk from source to target peg
        print(f"Move disk {n} from {source} to {target}")
        
        # Move the n-1 disks from auxiliary peg to target peg
        move_disks(n-1, auxiliary, source, target)

# Define the number of disks and the pegs
num_disks = 3
source_peg = "A"
auxiliary_peg = "B"
target_peg = "C"

# Call the move_disks function
move_disks(num_disks, source_peg, auxiliary_peg, target_peg)