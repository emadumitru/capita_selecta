def move_disks(n, source, auxiliary, destination):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        move_disks(n-1, source, destination, auxiliary)
        
        # Move the nth disk from source to destination peg
        print(f"Move disk {n} from {source} to {destination}")
        
        # Move the n-1 disks from auxiliary to destination peg
        move_disks(n-1, auxiliary, source, destination)

# Number of disks
num_disks = 3

# Peg names
source_peg = "A"
auxiliary_peg = "B"
destination_peg = "C"

# Solve the Tower of Hanoi problem
move_disks(num_disks, source_peg, auxiliary_peg, destination_peg)